def main():
    S, K = map(str, input().split())
    K = int(K)
    S_list = list(S)
    S_list.sort()
    #print(S_list)
    import itertools
    S_list_permutation = list(itertools.permutations(S_list))
    #print(S_list_permutation)
    S_list_permutation_uniq = list(set(S_list_permutation))
    S_list_permutation_uniq.sort()
    #print(S_list_permutation_uniq)
    S_list_permutation_uniq_str = []
    for i in range(len(S_list_permutation_uniq)):
        S_list_permutation_uniq_str.append("".join(S_list_permutation_uniq[i]))
    #print(S_list_permutation_uniq_str)
    print(S_list_permutation_uniq_str[K-1])
