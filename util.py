import string


def get_pid(fn: str):
    pid = ""
    ind = 0
    for i, c in enumerate(fn):
        if c in string.digits:
            pid += c
        else:
            ind = i
            break
    ind += 2
    p = ""
    for c in fn[ind:]:
        if c in string.digits:
            p += c
        else:
            break
    return (pid, p)
