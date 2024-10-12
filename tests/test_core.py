from sgt_file_manager import compute


def test_compute():
    assert compute(["a", "bc", "abc"]) == "abc"
