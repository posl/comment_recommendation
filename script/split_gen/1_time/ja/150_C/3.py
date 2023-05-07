def main():
    n = int(input())
    p = input().split()
    q = input().split()
    p = [int(i) for i in p]
    q = [int(i) for i in q]
    p = list(map(lambda x: x - 1, p))
    q = list(map(lambda x: x - 1, q))
    # print(p)
    # print(q)
    # print(p.index(2))
    # print(q.index(2))
    import math
    from itertools import permutations
    # print(math.factorial(n))
    # print(list(permutations(range(1, n+1))))
    # print(list(permutations(range(1, n+1))).index(tuple(p)))
    # print(list(permutations(range(1, n+1))).index(tuple(q)))
    print(abs(list(permutations(range(1, n+1))).index(tuple(p)) - list(permutations(range(1, n+1))).index(tuple(q))))
