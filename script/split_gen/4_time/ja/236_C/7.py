def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    s = 0
    for i in range(N):
        if S[i] == T[s]:
            s += 1
            if s == M:
                break
    for i in range(N):
        if S[i] == T[s]:
            print("Yes")
            s += 1
            if s == M:
                break
        else:
            print("No")
