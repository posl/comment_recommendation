def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(n):
        a[i] = a[i] / 2
    for i in range(m):
        a.append(a.pop() / 2)
    print(int(sum(a)))

if __name__ == '__main__':
    main()