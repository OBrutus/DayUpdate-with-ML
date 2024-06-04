DEFAULT_ESCAPE_SEQUENCE_BLACKLIST = set(['\n', '\t'])


def remove_spaces(
    s: str,
    times: int = 2
) -> str:
    res = ''
    count = 0
    for char in s:
        if char == ' ':
            count += 1
            continue

        if count > 0 and times != 1:
            count %= times
            # to make sanity while reading
            count = max(1, count)

        res += ' ' * count
        res += char

        count = 0

    return res


def remove_escape_sequence(
    s: str,
    removal: set = DEFAULT_ESCAPE_SEQUENCE_BLACKLIST,
) -> str:
    res = ''

    for char in s:
        if char in removal:
            continue
        res += char

    return res
