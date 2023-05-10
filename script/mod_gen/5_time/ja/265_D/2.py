def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if i < j < k < l:
                        if A[i] + A[i+1] + A[j-1] == P:
                            if A[j] + A[j+1] + A[k-1] == Q:
                                if A[k] + A[k+1] + A[l-1] == R:
                                    ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()