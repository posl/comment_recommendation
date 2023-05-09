def get_ints():
    return [ int(s) for s in input().split() ]
N, M = get_ints()
Ls = []
Rs = []
for i in range(M):
    L, R = get_ints()
    Ls.append(L)
    Rs.append(R)
L = max(Ls)
R = min(Rs)
print(max(0, R - L + 1))

if __name__ == '__main__':
    get_ints()