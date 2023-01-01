from pathlib import Path

from course.models import Author
from publish.document import document_body
from publish.files import write_file, read_file
from publish.text import text_lines, word_count
from workshop.resize_image import create_cover_images

from .models import Book, Content
from .pub import book_context, import_books, show_all_books


def book_outline(book):
    outline = ""
    for p in book_context(book)["parts"]:
        outline += p["part"].title + "\n"
        for c in p["chapters"]:
            path = Path(c.part.book.doc_path) / c.document
            md = document_body(read_file(path))
            for line in text_lines(md):
                if line.startswith("#"):
                    outline += line.replace("#", "    ")[1:] + "\n"
            outline += "\n"
    return outline


def create_book_outlines():
    for book in Book.objects.all():
        write_book_outline(book)


# def rebuild_books():
#     # Book.objects.all().delete()
#     import_books()
#     create_book_outlines()
#     update_word_counts()
#     word_count_books()
#     return show_all_books()


# def update_word_counts():
#     for book in Book.objects.all():
#         for p in book_context(book)["parts"]:
#             part = p["part"]
#             path = Path(part.book.doc_path) / part.document
#             md = document_body(read_file(path))
#             part.words = word_count(md)
#             for c in p["chapters"]:
#                 path = Path(c.part.book.doc_path) / c.document
#                 md = document_body(read_file(path))
#                 c.words = word_count(md)
#                 part.words += c.words
#                 c.save()
#             part.save()


# def word_count_books():
#     for book in Book.objects.all():
#         words = 0
#         outline = ""
#         for p in book_context(book)["parts"]:
#             part = p["part"]
#             outline += f"\n{part.title} ({part.words} words)\n\n"
#             words += part.words
#             for c in p["chapters"]:
#                 outline += f"    {c.title} ({c.words} words)\n"
#         outline = f"Book Word Count\n\n{book.title} ({words} words)\n" + outline
#         path = Path("Documents/markseaman.info") / book.name / "Words.ol"
#         write_file(path, outline)


def write_book_outline(book):
    outline = book_outline(book)
    path = Path("Documents/markseaman.info") / book.name / "Outline.ol"
    # print(path)
    write_file(path, outline)


# def test_book_covers():
#     rebuild_books()
#     # resize_book_cover()

#     path = "Documents/images/CoverArtwork/poem-cover.png"
#     create_cover_images(path)
#     # crop_cover_image()


# def show_book_content():
#     print(books_toc())
# for x in Author.objects.all():
#     print(x)
# for x in Book.objects.all():
#     print(x)
# # for x in Chapter.objects.all():
# #     print(x)
# print("Authors", len(Author.objects.all()))
# print("Book", len(Book.objects.all()))
# # print("Chapters", len(Chapter.objects.all()))
# # assert len(Author.objects.all()) == 1
# assert len(Book.objects.all()) == 4
# # assert len(Chapter.objects.all()) == 157
