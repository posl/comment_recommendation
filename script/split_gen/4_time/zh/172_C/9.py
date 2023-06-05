def solve():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.append(0)
    B.append(0)
    A.sort()
    B.sort()
    ans = 0
    i = 0
    j = 0
    while K > 0:
        if i < N and j < M:
            if A[i] < B[j]:
                if K > A[i]:
                    K -= A[i]
                    ans += 1
                    i += 1
                else:
                    break
            else:
                if K > B[j]:
                    K -= B[j]
                    ans += 1
                    j += 1
                else:
                    break
        elif i < N:
            if K > A[i]:
                K -= A[i]
                ans += 1
                i += 1
            else:
                break
        elif j < M:
            if K > B[j]:
                K -= B[j]
                ans += 1
                j += 1
            else:
                break
        else:
            break
    print(ans)
