from urllib.request import urlopen


def get_html_from_web(
        url: str
) -> tuple[str, bool]:
    if 1 == 1:
        import repository_layer
        location = "GkToday/html.html"
        return repository_layer.raw_file_read(location), False

    client = urlopen(url)
    content = client.read()
    client.close()
    return content, False
