#!/usr/bin/env python3
"""Generate deterministic Colab notebooks from the model registry."""
import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def render(model):
    path = ROOT / 'templates' / f"{model['task']}.ipynb"
    notebook = json.loads(path.read_text(encoding='utf-8'))
    values = {key: str(value) for key, value in model.items()}
    values['model_name_repr'] = repr(model.get('model_name', ''))
    for index, cell in enumerate(notebook['cells']):
        cell['id'] = f"{model['id']}-{index:02d}"
        cell['source'] = ''.join(cell['source']).format_map(values).splitlines(keepends=True)
        if cell['cell_type'] == 'code':
            cell['execution_count'] = None
            cell['outputs'] = []
    notebook['metadata']['hub_model_id'] = model['id']
    return json.dumps(notebook, ensure_ascii=False, indent=1) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    registry = yaml.safe_load((ROOT / 'configs/models.yaml').read_text(encoding='utf-8'))
    if registry.get('schema_version') != 1:
        raise ValueError('Unsupported registry schema')
    for model in registry['models']:
        target = ROOT / model['notebook']
        content = render(model)
        if args.check:
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Generated notebook differs: {target}')
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')
            print(target.relative_to(ROOT))


if __name__ == '__main__':
    main()
