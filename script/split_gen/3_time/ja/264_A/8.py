def main():
    s = input()
    L, R = map(int, s.split())
    print(s[L-1:R])
