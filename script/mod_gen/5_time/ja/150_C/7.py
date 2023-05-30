def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    def permutation(n):
        if n == 1:
            return [[1]]
        else:
            return [[n] + p for p in permutation(n-1)] + [p + [n] for p in permutation(n-1)]
    def index(l, p):
        for i, v in enumerate(l):
            if v == p:
                return i
    print(abs(index(permutation(n), p) - index(permutation(n), q)))
main()
