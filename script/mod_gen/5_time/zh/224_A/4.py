def get_suffix(s):
    if s.endswith("er"):
        return "er"
    elif s.endswith("ist"):
        return "ist"
    else:
        return "error"

if __name__ == '__main__':
    get_suffix()