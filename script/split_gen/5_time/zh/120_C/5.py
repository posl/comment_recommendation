def main():
    s = input()
    n = len(s)
    r = s.count("0")
    b = s.count("1")
    print(min(r, b) * 2)
