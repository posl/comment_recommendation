def get_lexicographically_smallest_permutation(N, P):
    sorted_P = sorted(P)
    sorted_P.reverse()
    sorted_P.append(0)
    sorted_P.reverse()
    return sorted_P
N = int(input())
P = list(map(int, input().split()))
print(" ".join(map(str, get_lexicographically_smallest_permutation(N, P))))
