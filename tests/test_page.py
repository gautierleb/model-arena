from app import page


def test_the_page_says_hello() -> None:
    assert "<h1>Hello</h1>" in page()
