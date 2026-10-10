"""The page this project serves."""


def page() -> str:
    """The HTML of the home page."""
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        "<title>Home</title></head><body><main><h1>Hello</h1></main></body></html>"
    )
