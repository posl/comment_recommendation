def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]
    for a in A:
        S.append(S[-1]+a)
    ans = "No"
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if P == S[i+1]-S[0] and Q == S[j+1]-S[i+1] and R == S[k+1]-S[j+1]:
                    ans = "Yes"
                    break
            if ans == "Yes":
                break
        if ans == "Yes":
            break
    print(ans)
