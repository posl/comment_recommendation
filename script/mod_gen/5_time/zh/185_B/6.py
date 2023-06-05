def main():
    n,m,t = map(int,input().split())
    A = [0 for i in range(m)]
    B = [0 for i in range(m)]
    for i in range(m):
        A[i],B[i] = map(int,input().split())
    ans = 'Yes'
    for i in range(m):
        if i == 0:
            if A[i] != 1:
                ans = 'No'
                break
            if A[i] == 1 and B[i] == t:
                ans = 'No'
                break
            if B[i] == t:
                break
            if B[i] > A[i] + 1:
                ans = 'No'
                break
            if B[i] <= A[i] + 1:
                n -= (B[i] - A[i])
        elif i == m-1:
            if A[i] == t:
                break
            if A[i] > B[i-1] + 1:
                ans = 'No'
                break
            if B[i] > A[i] + 1:
                ans = 'No'
                break
            if B[i] <= A[i] + 1:
                n -= (B[i] - A[i])
        else:
            if A[i] > B[i-1] + 1:
                ans = 'No'
                break
            if B[i] > A[i] + 1:
                ans = 'No'
                break
            if B[i] <= A[i] + 1:
                n -= (B[i] - A[i])
    if ans == 'Yes':
        if n <= 0:
            ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()