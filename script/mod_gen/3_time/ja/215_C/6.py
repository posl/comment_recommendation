def getPermutations(S):
    if len(S) == 1:
        return S
    else:
        L = []
        for i in range(len(S)):
            a = S[i]
            b = S[0:i] + S[i+1:]
            for x in getPermutations(b):
                L.append(a + x)
        return L
S, K = input().split()
K = int(K)
L = getPermutations(S)
L.sort()
print(L[K-1])

if __name__ == '__main__':
    getPermutations()