def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        print(a-1, b)
    elif u == t:
        print(a, b-1)
    else:
        print(a, b)

if __name__ == '__main__':
    main()