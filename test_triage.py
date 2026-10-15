import pytest

from triage import classify


@pytest.mark.parametrize(
    "title, expected",
    [
        ("App crashes when I click save", "bug"),
        ("Error 500 on login", "bug"),
        ("Add dark mode", "feature"),
        ("Support CSV export", "feature"),
        ("How do I reset my password?", "question"),
        ("Is there an API?", "question"),
    ],
)
def test_classify(title, expected):
    assert classify(title) == expected