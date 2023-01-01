from publish.files import recursive_files
from probe.probe import check_file_count
from publish.shell import shell


def test_git_files():
    return "Git " + check_file_count(recursive_files(".git"), 2000, 9000)


def test_git_status():
    return shell("git status")
