from pathlib import Path

from sgt_file_manager import cmd_scan

TMP_TEST_DIR = Path("tmp_test_dir")


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
    for file in files:
        with open(TMP_TEST_DIR / file, "w") as f:
            f.write("test data")


def test_cmd_scan():
    create_files()
    output_file = TMP_TEST_DIR / "output.json"
    data = cmd_scan(TMP_TEST_DIR, output_file)
    assert len(data) == 10
    assert data[0]["file_name"] == "file1.txt"
    assert data[0]["file_size"] == 8
