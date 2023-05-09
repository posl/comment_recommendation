def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0]
    for i in range(N-1):
        if S[i] == 'A' and S[i+1] == 'C':
            l.append(l[-1] + 1)
        else:
            l.append(l[-1])
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1] - l[l_i-1])
