import subprocess
import sys


def run(*args):
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
        cwd="src",
        check=False,
    )


def test_help():
    proc = run("--help")
    assert proc.returncode == 0


def test_success():
    proc = run("calc", "2+3*4")
    assert proc.returncode == 0
    assert proc.stdout.strip() == "14.0"


def test_error_stderr_and_code_two():
    proc = run("calc", "1/0")
    assert proc.returncode == 2
    assert proc.stderr.strip() != ""