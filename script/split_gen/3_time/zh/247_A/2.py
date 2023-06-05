def problem247_a(s):
    l = list(s)
    l.append('0')
    l.pop(0)
    return "".join(l)
