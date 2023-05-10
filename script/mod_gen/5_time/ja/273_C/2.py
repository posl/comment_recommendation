def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 1
    ans = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += count*(count-1)//2
            count = 1
        else:
            count += 1
    ans += count*(count-1)//2
    for i in range(N):
        if i == 0:
            print(ans)
        elif A[i-1] != A[i]:
            ans -= count*(count-1)//2
            print(ans)
        else:
            print(ans)

if __name__ == '__main__':
    main()