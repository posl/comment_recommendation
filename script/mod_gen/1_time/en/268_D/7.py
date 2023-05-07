def solve(N, M, S, T):
    if N == 1:
        for i in range(3, 17):
            if S[0] + '_' * (i - len(S[0])) not in T:
                return S[0] + '_' * (i - len(S[0]))
        return -1
    else:
        for i in range(3, 17):
            for j in range(3, 17):
                if i + j < 3 or i + j > 16:
                    continue
                for s1 in S[0]:
                    for s2 in S[1]:
                        if s1 + '_' * (i - 1) + s2 + '_' * (j - 1) + S[2] not in T:
                            return s1 + '_' * (i - 1) + s2 + '_' * (j - 1) + S[2]
        return -1
N, M = map(int, input().split())
S = []
T = []
for i in range(N):
    S.append(input())
for i in range(M):
    T.append(input())
print(solve(N, M, S, T))
I am trying to get the following code to work. I have a list of lists, and I want to get a list of the values in the first column. The code below is what I have so far, but it doesn’t work. Any help is appreciated.
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b = []
for i in a:
    b.append(i[0])
print(b)
I have a list of lists and I want to get a list of the values in the first column. The code below is what I have so far, but it doesn’t work. Any help is appreciated.
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b = []
for i in a:
    b.append(i[0])
print(b)
I have a list of lists and I want to get a list of the values in the first column. The code below is what I have so far, but it doesn’t work. Any help is appreciated.
a = [[1,

if __name__ == '__main__':
    solve()