from pathlib import Path

from probe.probe import check_files
from publish.text import char_fix_files

docs = Path("Documents")


def test_documents_bacs200():
    return check_files(docs / "shrinking-world.com" / "bacs200", 70, 80)


def test_documents_bacs350():
    return check_files(docs / "shrinking-world.com" / "bacs350", 180, 250)


def test_documents_cs350():
    return check_files(docs / "shrinking-world.com" / "cs350", 120, 130)


def test_documents_info():
    return check_files(docs / "markseaman.info", 2800, 3000)


def test_documents_images():
    return check_files(Path("static") / "images", 480, 550)


def test_documents_fix_chars():
    return char_fix_files("Documents")


def test_documents_seamanslog():
    return check_files(docs / "seamanslog.com", 300, 450)


def test_documents_seamansguide():
    return check_files(docs / "seamansguide.com", 420, 440)


def test_documents_spiritual():
    return check_files(docs / "spiritual-things.org", 950, 1300)


def test_documents_shrinking_world():
    return check_files(docs / "shrinking-world.com", 580, 610)


def test_documents_mark():
    return check_files(docs / "markseaman.org", 10, 20)


def test_documents_family():
    return check_files(docs / "seamanfamily.org", 5, 20)
