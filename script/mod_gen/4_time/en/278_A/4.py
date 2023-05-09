def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(a.pop(0))
    print(*a)

if __name__ == '__main__':
    main()