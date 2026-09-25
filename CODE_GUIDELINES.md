# Code and maintenance guidelines

This repository is a reference release of thesis work. These notes document
maintenance expectations; they do not establish an external contribution
program.

- Keep hardware communication, inference, and analysis responsibilities separate.
- Use repository-relative paths or explicit CLI arguments; do not commit local drive paths, credentials, datasets, or model binaries.
- Add module docstrings and docstrings to public functions and CLI entry points.
- Validate sensor shape and numeric values at serial/inference boundaries.
- Keep sensor order explicit: `thumb`, `index`, `middle`, `ring`, `little`.
- Record model name, preprocessing, class mapping, and evaluation split with published results.
- Do not describe Python inference as Arduino deployment until an on-device implementation is tested.
- Cite the IEEE paper, thesis report, dataset, and repository when presenting results.

Before sharing changes:

```bash
python -m py_compile flex_to_num.py read_from_arduino.py
git diff --check
```
