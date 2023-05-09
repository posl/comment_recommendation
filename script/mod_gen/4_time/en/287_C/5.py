def main():
    n, m = map(int, input().split())
    e = [0 for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        e[a-1] += 1
        e[b-1] += 1
    for i in range(n):
        if e[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()