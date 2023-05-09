def swap(s, a, b):
    if a < b:
        return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    else:
        return s[:b-1] + s[a-1] + s[b:a-1] + s[b-1] + s[a:]
N = int(input())
S = input()
Q = int(input())
s1 = S[:N]
s2 = S[N:]
for i in range(Q):
    T,A,B = map(int, input().split())
    if T == 1:
        if A <= N and B <= N:
            s1 = swap(s1, A, B)
        elif N < A and N < B:
            s2 = swap(s2, A-N, B-N)
        else:
            s1, s2 = s2, s1
    else:
        s1, s2 = s2, s1
print(s1 + s2)
