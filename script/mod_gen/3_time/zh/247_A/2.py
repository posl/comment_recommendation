def problem247_a(s):
    l = list(s)
    l.append('0')
    l.pop(0)
    return "".join(l)

if __name__ == '__main__':
    problem247_a()