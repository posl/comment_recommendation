def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, P, Q, R)
    #print(A)
    ans = "No"
    for i in range(N-3+1):
        x = A[i]
        for j in range(i+1, N-2+1):
            y = A[j]
            for k in range(j+1, N-1+1):
                z = A[k]
                for l in range(k+1, N+1):
                    w = A[l]
                    if (x+y+z+w) == (P+Q+R) and (x+y) == P and (y+z) == Q and (z+w) == R:
                        ans = "Yes"
                        break
                if ans == "Yes":
                    break
            if ans == "Yes":
                break
        if ans == "Yes":
            break
    print(ans)
solve()
