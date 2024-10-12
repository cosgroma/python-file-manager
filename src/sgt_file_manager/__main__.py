"""
Entrypoint module, in case you use `python -msgt_file_manager`.


Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

from sgt_file_manager.cli import sgt_kb_main

if __name__ == "__main__":
    sgt_kb_main()
