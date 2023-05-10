def main():
    n = int(input())
    t = list(map(int, input().split()))
    if n == 1:
        print(t[0])
    elif n == 2:
        print(max(t[0], t[1]))
    else:
        t.sort()
        print(max(t[0] + t[-2], t[1] + t[-1]))

if __name__ == '__main__':
    main()