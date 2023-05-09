def main():
    s = input()
    l, r = map(int, s.split())
    s = "atcoder"
    print(s[l-1:r])
