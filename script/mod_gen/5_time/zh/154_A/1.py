def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        print(a-1, b)
    elif t == u:
        print(a, b-1)

if __name__ == '__main__':
    main()