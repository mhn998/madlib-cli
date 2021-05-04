import pytest
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("samples/short_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_parts = parse_template(read_template("samples/short_template.txt"),isInput=False)
    expected_parts = ["Adjective", "Adjective", "Noun"]
    assert actual_parts == expected_parts


def test_merge():
    actual = merge(["dark", "stormy", "night"], parse_template(read_template("samples/short_template.txt"),isInput=False) , read_template("samples/short_template.txt"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "missing.txt"
#         read_template(path)

