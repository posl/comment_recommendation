def my_permutations(S):
    if len(S) == 1:
        return S
    else:
        result = []
        for i in range(len(S)):
            for j in my_permutations(S[:i] + S[i + 1:]):
                result.append(S[i] + j)
        return result
S = input()
print(len(my_permutations(S)))
