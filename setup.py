#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with Path(__file__).parent.joinpath(*names).open(encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


def get_requirements(filename="requirements.txt"):
    if not Path(filename).exists():
        print(f"WARNING: {filename} not found")
        return []
    with Path.open(Path(filename)) as f:
        requires = [line.replace("\n", "") for line in f.readlines()]
    return requires


setup(
    name="sgt-file-manager",
    version="0.0.0",
    license="MIT",
    description="File Management Library",
    long_description=read("README.md"),
    author="Mathew Cosgrove",
    author_email="cosgroma@gmail.com",
    url="https://github.com/cosgroma/python-file-manager",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[path.stem for path in Path("src").glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/cosgroma/python-file-manager/blob/master/CHANGELOG.md",
        "Issue Tracker": "https://github.com/cosgroma/python-file-manager/issues",
    },
    keywords=[
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    python_requires=">=3.8",
    install_requires=get_requirements(),
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=='3.8'": ["backports.zoneinfo"],
    },
    entry_points={
        "console_scripts": [
            "sgt-kb = sgt_file_manager.cli:sgt_kb_main",
        ]
    },
)
