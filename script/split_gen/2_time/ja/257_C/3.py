def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    S = S[::-1]
    W = W[::-1]
    ans = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] < W[ans]:
                ans = i
        else:
            if W[i] > W[ans]:
                ans = i
    print(ans+1)
