def solve():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [int(i) for i in input().split()]
    def permutation_index(p):
        index = 0
        for i in range(len(p)):
            index += p[i] - 1
            index *= len(p) - i - 1
        return index
    print(abs(permutation_index(p) - permutation_index(q)))
solve()
