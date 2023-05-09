def main():
    s = input()
    print(-1 if len(set(s)) == 1 else [c for c in s if s.count(c) == 1][0])
main()
