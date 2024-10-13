from datetime import datetime
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


def get_datetime_from_iso(iso_str):
    return datetime.fromisoformat(iso_str)


def test_cmd_scan():
    create_files()
    output_file = TMP_TEST_DIR / "output.json"
    data = cmd_scan(TMP_TEST_DIR, output_file)
    assert len(data) > 0

    # assert data[0]["created"] < test_datetime
    #     file_info.update(
    #     {
    #         "id": str(uuid.UUID(bytes=file_hash[:16])),
    #         "name": Path(file_path).name,
    #         "full_path": str(file_path),
    #         # "relative_path": str(Path(file_path).relative_to(Path.cwd())),
    #         "type": mimetypes.guess_type(file_path, False)[0] or "UNK",
    #         "size": file_stats.st_size,
    #         "last_modified": datetime.fromtimestamp(file_stats.st_mtime, tz=datetime.now().astimezone().tzinfo).isoformat(),
    #         "created": datetime.fromtimestamp(file_stats.st_ctime, tz=datetime.now().astimezone().tzinfo).isoformat(),
    #         "author": file_stats.st_uid,
    #         "group": file_stats.st_gid,
    #         "permissions": oct(file_stats.st_mode & 0o777),
    #         "info": file_details.strip(),
    #     }
    # )
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
    for file in TMP_TEST_DIR.iterdir():
        file.unlink()
    TMP_TEST_DIR.rmdir()
