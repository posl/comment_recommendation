def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        if a[i] == 1:
            b[i] = 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1)

if __name__ == '__main__':
    main()