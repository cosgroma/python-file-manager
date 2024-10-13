import json
from datetime import datetime
from pathlib import Path

from sgt_file_manager import cmd_scan
from sgt_file_manager import get_file_list
from sgt_file_manager.core import DIR_TO_SKIP

TMP_TEST_DIR = Path(__file__).parent / "tmp"


def create_files():
    files = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
        "file4.txt",
        "file5.txt",
        "file6.txt",
        "file7.txt",
        "file8.txt",
        "file9.txt",
        "file10.txt",
    ]
    # create test directory
    Path.mkdir(TMP_TEST_DIR, exist_ok=True)
    for file in files:
        with Path.open(TMP_TEST_DIR / file, "w") as f:
            f.write("test data")


def create_skip_dirs():
    dirs = DIR_TO_SKIP
    # create test directory
    Path.mkdir(TMP_TEST_DIR, exist_ok=True)
    for dir in dirs:
        Path.mkdir(TMP_TEST_DIR / dir, exist_ok=True)


def cleanup():
    # cleanup
    for file in TMP_TEST_DIR.iterdir():
        if Path.is_file(file):
            file.unlink()
        else:
            file.rmdir()
    TMP_TEST_DIR.rmdir()


def test_get_file_list():
    create_files()
    files = get_file_list(TMP_TEST_DIR)
    assert len(files) == 10

    # cleanup
    cleanup()


def test_get_file_list_skip_dirs():
    create_skip_dirs()
    files = get_file_list(TMP_TEST_DIR)
    assert len(files) == 0
    # cleanup
    cleanup()


def test_cmd_scan():
    create_files()
    output_file = TMP_TEST_DIR / "output.json"
    data = cmd_scan(TMP_TEST_DIR, output_file)
    # check output_file exists
    assert output_file.exists()
    # check if output_file is a json file
    assert output_file.suffix == ".json"
    # load data from output_file
    with Path.open(output_file, "r") as f:
        json_data = json.load(f)
    assert len(json_data) > 0

    # assert data and json_data are equal
    assert len(data) == len(json_data)

    # check data is a list
    assert len(data) > 0
    assert len(data[0]["name"]) > 0
    assert len(data[0]["full_path"]) > 0
    assert len(data[0]["type"]) > 0
    assert data[0]["size"] > 0
    assert len(data[0]["last_modified"]) > 0
    assert datetime.fromisoformat(data[0]["created"]) is not None
    assert data[0]["author"] > 0
    assert data[0]["group"] > 0
    assert len(data[0]["permissions"]) > 0
    assert len(data[0]["info"]) > 0

    # cleanup
    cleanup()
