def lower_case(s, k):
    return s[:k-1] + s[k-1].lower() + s[k:]

if __name__ == '__main__':
    lower_case()