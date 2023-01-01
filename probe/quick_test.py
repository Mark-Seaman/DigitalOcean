from re import sub
from django.utils.timezone import make_aware, localdate
from pathlib import Path

from course.course import get_course, weekly_content
from course.lesson import prepare_lesson
from publish.days import tomorrow
from publish.import_export import import_pub
from publish.pub import build_pubs, get_pub, get_pub_contents, show_pubs
from publish.models import Content, Pub
from course.course import accordion_data
from publish.seamanslog import extract_message, random_article, random_post
from publish.toc import table_of_contents
from task.todo import edit_blog_files, edit_review_file, edit_todo_list, edit_toot_file

import toot


def quick_test():
    # print("No quick test defined")
    # pubs()
    todo()


def todo():
    print("TODO")
    # edit_todo_list()
    # edit_review_file()
    # edit_toot_file()
    # edit_blog_files()
    print(random_post("journey"))
    # article = random_article()
    # print(extract_message(article["doc"], article["url"]))


def pubs():
    print("Build Pubs")
    p = get_pub("tech")
    import_pub(p)
    contents = get_pub_contents(p)
    print(table_of_contents(p, contents))
    # build_pubs()
    # print(show_pubs())


def write_webapps_contents():
    csv = ""
    x = 1
    for i, row in enumerate(range(14)):
        chapter = i + 1
        csv += f"chapter/{i+1:02}.md,{chapter}\n"
        x += 1
        csv += f"skill/{i*3+1:02}.md,{chapter},{x}\n"
        x += 1
        csv += f"skill/{i*3+2:02}.md,{chapter},{x}\n"
        x += 1
        csv += f"skill/{i*3+3:02}.md,{chapter},{x}\n"
        x += 1
        csv += f"demo/{i+1:02}.md,{chapter},{x}\n"
        x += 1
        csv += f"project/{i+1:02}.md,{chapter},{x}\n"
        x += 1
    Path("Documents/seamansguide.com/webapps/_content.csv").write_text(csv)


def courses():

    print("Build Courses")
    weeks = weekly_content(get_course("bacs350"))
    weeks = accordion_data()
    for w in weeks:
        print(w)
    # create_course(**bacs350_options())
    # prepare_lesson(10)
    # prepare_lesson(11)
    # import_all_courses()

    # name = "write"
    # create_blog(name)

    # build_blogs()

    # b = Pub.objects.all().values()[0]
    # print(b)
    # f = f"blog.json"
    # print(f)
    # write_json(f, b)
    # book = get_book("journey")
    # for part in list_parts(book):
    #     print(part)
    #     for c in part["chapters"]:
    #         print(c)

    # print(test_book_import())

    # print("Show course content")
    # print(test_export_courses())
