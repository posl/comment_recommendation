def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, P, Q, R)
    for i in range(N):
        if A[i] > R:
            break
        for j in range(i+1, N):
            if A[j] > R:
                break
            for k in range(j+1, N):
                if A[k] > R:
                    break
                for l in range(k+1, N):
                    if A[l] > R:
                        break
                    if (A[i] + A[i+1] + A[j] + A[j+1] + A[k] + A[k+1] + A[l] + A[l+1]) == (P + Q + R):
                        print("Yes")
                        return
    print("No")
