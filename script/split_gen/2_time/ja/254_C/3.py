def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K % 2 == 0:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
    else:
        ans = 'No'
        for i in range(N):
            if i == 0:
                if A[i] <= A[i+1]:
                    ans = 'Yes'
                else:
                    ans = 'No'
                    break
            elif i == N-1:
                if A[i] >= A[i-1]:
                    ans = 'Yes'
                else:
                    ans = 'No'
                    break
            else:
                if A[i-1] <= A[i] <= A[i+1]:
                    ans = 'Yes'
                else:
                    ans = 'No'
                    break
        print(ans)
