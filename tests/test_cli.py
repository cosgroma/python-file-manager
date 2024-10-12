import subprocess


def test_main():
    assert subprocess.check_output(["sgt-kb", "foo", "foobar"], text=True) == "foobar\n"
