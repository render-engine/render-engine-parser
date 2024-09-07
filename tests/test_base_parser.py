import frontmatter
import pytest

from render_engine_parser.base_parsers import BasePageParser, parse_content


@pytest.fixture()
def base_content() -> str:
    return """
---
title: This is a Test
---

# This is a Test"""


@pytest.fixture()
def base_content_path(tmp_path, base_content):
    """Returns the path to a test file"""
    d = tmp_path / "test_page.md"
    d.write_text(base_content)
    return d


def test_parse_content(base_content):
    """
    Tests that parse_content returns a split of the content and attributes
    Currently python-frontmatter is used to do this. This test is here to
    ensure that the API is consistent.

    Base Content is an example of a markdown file with frontmatter.
    """

    expected_result = ({"title": "This is a Test"}, "# This is a Test")
    assert expected_result == parse_content(base_content)


def test_base_parser_parse_content(base_content):
    """
    Tests for the BasePageParser pase_content Functionality.
    This assures that the API is consistently calling the parse_content
    """

    expected_result = ({"title": "This is a Test"}, "# This is a Test")
    assert expected_result == BasePageParser.parse_content(base_content)


def test_base_parser_parse_content_path(base_content_path):
    """
    Tests for the BasePageParser parse_content_path Functionality.
    This assures that the API is consistently calling the parse_content
    """

    expected_result = ({"title": "This is a Test"}, "# This is a Test")
    assert expected_result == BasePageParser.parse_content_path(base_content_path)


def test_base_parser_net_entry():
    data = BasePageParser.create_entry(
        content="This is a Test",
        title="Untitled Entry",
        slug="untitled-entry",
    )

    post = frontmatter.loads(data)
    assert post["title"] == "Untitled Entry"
    assert post["slug"] == "untitled-entry"
    assert post.content == "This is a Test"
