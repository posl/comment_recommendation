def calc(N, S):
    if N == 1:
        if S == "AND":
            return 2
        else:
            return 1
    if S == "AND":
        return 2**(N+1)-2**(N)
    else:
        return 2**(N+1)-1
N = int(input())
S = []
for i in range(N):
    S.append(input())
print(calc(N, S))

if __name__ == '__main__':
    calc()