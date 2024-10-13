#!/usr/bin/env python
"""
@package   core
Details:    This module contains the core functionality for the file manager
Created:   Saturday, October 12th 2024, 3:26:09 pm
-----
Last Modified: 10/12/2024 06:50:01
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "core.py"
__version__ = "0.1.0"

import hashlib
import json
import mimetypes
import os
import subprocess
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

# from progress.bar import Bar
from tqdm import tqdm


def file_path_has_str(path: Path, str: str) -> bool:
    """Check if a file path contains a string

    Args:
        path (Path): The path to the file
        str (str):  The string to check for

    Returns:
        bool:
    """
    return str in path


def get_hash_of_content(file_path: Path) -> str:
    """Get the hash of the content of a file

    Args:
        file_path (Path): The file to hash

    Returns:
        str: The hash of the file content
    """
    sha256_hash = hashlib.sha256()
    with Path.open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_file_info(file_path: Path) -> Dict[str, Any]:
    """Gather detailed information about a file.

    Args:
        root (Path): The root directory
        file (Path): The file to get information for

    Returns:
        _type_: _description_
    """
    file_info: Dict[str, Any] = {}
    file_info["name"] = Path(file_path).name
    file_info["metadata"] = []
    try:
        file_stats = Path.stat(file_path)
        result = subprocess.run(["file", "-b", file_path], capture_output=True, text=True)
        file_details = result.stdout

        # make secure hash
        file_hash = hashlib.sha256(f"{file_path}".encode()).digest()

        file_info.update(
            {
                "id": str(uuid.UUID(bytes=file_hash[:16])),
                "name": Path(file_path).name,
                "full_path": str(file_path),
                # "relative_path": str(Path(file_path).relative_to(Path.cwd())),
                "type": mimetypes.guess_type(file_path, False)[0] or "UNK",
                "size": file_stats.st_size,
                "last_modified": datetime.fromtimestamp(file_stats.st_mtime, tz=datetime.now().astimezone().tzinfo).isoformat(),
                "info": file_details.strip(),
            }
        )

        return file_info
    except Exception as e:
        print(f"\nERROR getting info for {file_info['name']} - {e} - SKIPPING")
        file_info["metadata"].append(
            {"type": "dev-status", "dev-status": {"parsed": False, "error": {"type": str(type(e)), "message": str(e)}}}
        )
        return file_info


DIR_TO_SKIP = [
    ".git",
    ".github",
    ".vscode",
    ".idea",
    ".pytest_cache",
    "__pycache__",
    ".tox",
    "build",
    ".venv",
    "dist",
]

FILE_EXT_TO_SKIP = [".pyc", ".pyo", ".pyd", ".so", ".dll", ".exe", ".o", ".a", ".lib", ".obj", ".bin", ".dat", ".db"]


def get_file_list(directory: Path) -> List[Path]:
    """Get a list of files in a directory skipping the files that have a parent directory in DIR_TO_SKIP

    Args:
        directory (Path): The directory to scan

    Returns:
        List[Path]: The list of files
    """
    file_list = []
    for root, _, files in os.walk(directory):
        if len(files) == 0:
            continue
        # skip directories we don't want to scan
        for file in files:
            # remove directory string from file path
            file_path_no_dir = Path(root).relative_to(directory) / file
            # get first part of file_path_no_dir
            # if it is in DIR_TO_SKIP, skip
            if str(file_path_no_dir).split("/")[0] in DIR_TO_SKIP:
                continue
            if file_path_no_dir.suffix in FILE_EXT_TO_SKIP:
                continue
            file_list.append(Path(root) / file)
    return file_list


def scan_directory(directory: Path) -> List[Dict[str, Any]]:
    """Scan the specified directory and return file details.

    Args:
        directory (Path): The directory to scan

    Returns:
        List[Dict[str, Any]]: The file information
    """
    file_info = []

    files = get_file_list(directory)
    if not files or len(files) == 0:
        print(f"No files found in {directory}")
        return file_info

    for file in tqdm(files):
        try:
            # measure execution time
            # start = datetime.now()
            info = get_file_info(file)
            # end = datetime.now()
            # duration = end - start
            if info:
                file_info.append(info)
        except Exception as e:
            print(f"\nERROR getting info for {file} - {e!s} - SKIPPING")
    return file_info


def cmd_scan(directory: Path, output_file: Path) -> List[Dict[str, Any]]:
    """Scan a directory and write the results to a file

    Args:
        directory (Path): The directory to scan
        output_file (Path): The file to write the results to

    Returns:
        file_info_list (List[Dict[str, Any]]): The data that was written to the file
    """
    dirpath = Path(directory).absolute()
    file_info_list = scan_directory(dirpath)
    with Path.open(output_file, "w") as json_file:
        json.dump(file_info_list, json_file, indent=4)
    return file_info_list
