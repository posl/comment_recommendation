def main():
    N = int(input())
    a = [1]
    for i in range(1, N):
        a.append(1)
        for j in range(i-1, 0, -1):
            a[j] += a[j-1]
    for i in range(N):
        print(*a[:i+1])

if __name__ == '__main__':
    main()