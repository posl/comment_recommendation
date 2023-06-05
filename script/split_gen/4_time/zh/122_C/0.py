def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N+1)
    for i in range(1, N):
        l[i+1] = l[i]
        if S[i-1:i+1] == "AC":
            l[i+1] += 1
    for i in range(Q):
        a, b = map(int, input().split())
        print(l[b] - l[a])
