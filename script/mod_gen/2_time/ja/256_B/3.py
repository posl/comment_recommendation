def main():
    N = int(input())
    A = list(map(int, input().split()))
    p = 0
    for i in range(N):
        p += A[i]
        if p >= 4:
            p -= 4
    print(p)

if __name__ == '__main__':
    main()