def unique(l):
    return list(set(l))
N = int(input())
S = [input() for i in range(N)]
print(len(unique(S)))
