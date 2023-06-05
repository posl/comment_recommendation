def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    def permutation_to_int(p):
        ret = 0
        for i in range(len(p)):
            ret += p[i] * 10 ** (len(p) - i - 1)
        return ret
    p_int = permutation_to_int(p)
    q_int = permutation_to_int(q)
    print(abs(p_int - q_int))
