def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                if (A[i]+A[j]+A[k])%P == 0 and (A[j]+A[k])%Q == 0 and (A[k])%R == 0:
                    ans = "Yes"
                    break
            if ans == "Yes":
                break
        if ans == "Yes":
            break
    print(ans)
