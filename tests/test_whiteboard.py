from itertools import zip_longest

from whiteboard import parse_accept_language


def test_parse_accept_language(test_case):
    header = test_case["header"]
    supported_languages = test_case["supported_languages"]
    expected = test_case["expected"]

    actual = parse_accept_language(header, supported_languages)
    sentinel = object()
    assert all(a == b for a, b in zip_longest(expected, actual, fillvalue=sentinel))
