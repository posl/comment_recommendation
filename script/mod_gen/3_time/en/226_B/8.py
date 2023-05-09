def main():
    N = int(input())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
    a.sort()
    a.append([0, 0])
    count = 0
    prev = [0, 0]
    for i in range(N+1):
        if a[i] == prev:
            count += 1
        prev = a[i]
    print(N-count)

if __name__ == '__main__':
    main()