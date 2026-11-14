#!/usr/bin/env python3
"""Static registry, notebook, and README checks; does not execute inference."""
import ast
import re
from pathlib import Path

import nbformat
import yaml

ROOT = Path(__file__).resolve().parents[1]
registry = yaml.safe_load((ROOT / 'configs/models.yaml').read_text(encoding='utf-8'))
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
assert registry['schema_version'] == 1
ids, paths = set(), set()
for model in registry['models']:
    for key in ('id','task','title','notebook','source_url','model_url','license','package','model_revision','status'):
        assert model.get(key), f"{model.get('id')}: missing {key}"
    assert model['task'] in ('asr','tts')
    assert model['status'] in ('unverified','verified')
    assert model['id'] not in ids and model['notebook'] not in paths
    ids.add(model['id']); paths.add(model['notebook'])
    if model['status'] == 'verified':
        log = model.get('verification_log')
        assert log and (ROOT / log).is_file(), f"{model['id']}: verified without log"
    path = ROOT / model['notebook']
    assert path.is_file(), path
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    assert nb.metadata.hub_model_id == model['id']
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue
        assert cell.execution_count is None and not cell.outputs, f'{path}: saved execution at {i}'
        source = '\n'.join(line for line in cell.source.splitlines() if not line.lstrip().startswith(('%','!')))
        ast.parse(source, filename=f'{path}:{i}')
        assert not re.search(r'(hf_[A-Za-z0-9]{20,}|HUGGING_FACE_HUB_TOKEN\s*=\s*[\'\"][^\'\"]+)', cell.source)
    relative = model['notebook']
    assert f']({relative})' in readme, f'README missing notebook link: {relative}'
    colab = f"https://colab.research.google.com/github/{registry['repository']}/blob/main/{relative}"
    assert colab in readme, f'README missing Colab link: {relative}'
    print(f'OK {relative}: nbformat, code syntax, no outputs, README links')
for path in (ROOT / 'notebooks').rglob('*.ipynb'):
    assert str(path.relative_to(ROOT)) in paths, f'unregistered notebook: {path}'
print('Static validation passed; GPU inference remains unverified unless a real log is recorded.')
