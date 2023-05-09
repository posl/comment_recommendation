def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        if i == 0 or A[i] != A[i-1]:
            cnt += i
    print(cnt)

if __name__ == '__main__':
    main()