def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    B = [0] * (10**6+1)
    for a in A:
        B[a] += 1
    ans = 0
    for a in A:
        if B[a] == 1:
            ans += 1
        else:
            for i in range(a,10**6+1,a):
                B[i] = 0
    print(ans)

if __name__ == '__main__':
    main()