def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        b.append(a[i])
        b.sort()
        if len(b) % 2 == 0:
            print(b[len(b) // 2 - 1])
        else:
            print(b[len(b) // 2])

if __name__ == '__main__':
    main()