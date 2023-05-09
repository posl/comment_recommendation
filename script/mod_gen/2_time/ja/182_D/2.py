def main():
    N = int(input())
    A = list(map(int,input().split()))
    max = 0
    for i in range(N):
        max += A[i]
        if max < 0:
            max = 0
    print(max)

if __name__ == '__main__':
    main()