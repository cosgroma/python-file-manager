import subprocess


def test_main():
    assert subprocess.check_output(["sgt-kb", "--help"], text=True).startswith("Usage: sgt-kb [OPTIONS] DIRECTORY")
