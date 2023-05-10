def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    def permutation(n):
        if n == 0:
            return [[]]
        else:
            return [[x] + y for x in range(n) for y in permutation(x)]
    def index(a, l):
        return l.index(a)
    print(abs(index(p, permutation(n)) - index(q, permutation(n))))

if __name__ == '__main__':
    main()