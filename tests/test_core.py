from pathlib import Path

from sgt_file_manager import cmd_scan

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


def test_cmd_scan():
    create_files()
    output_file = TMP_TEST_DIR / "output.json"
    data = cmd_scan(TMP_TEST_DIR, output_file)
    assert len(data) > 0
    # assert data[0]["name"] == "file1.txt"
    assert data[0]["file_size"] == 8
    # cleanup
    for file in TMP_TEST_DIR.iterdir():
        file.unlink()
    TMP_TEST_DIR.rmdir()
