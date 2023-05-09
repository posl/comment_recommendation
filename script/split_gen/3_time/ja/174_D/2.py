def main():
    N = int(input())
    s = input()
    R = [0 for i in range(N)]
    W = [0 for i in range(N)]
    for i in range(N):
        if s[i] == "R":
            R[i] = 1
        else:
            W[i] = 1
    for i in range(N-1):
        R[i+1] += R[i]
        W[i+1] += W[i]
    ans = N
    for i in range(N):
        ans = min(ans, i+1-R[i]+W[N-1]-W[i])
    print(ans)
