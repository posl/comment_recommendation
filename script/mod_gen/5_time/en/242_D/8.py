def solve():
    s = input()
    q = int(input())
    n = len(s)
    # 0: A
    # 1: B
    # 2: C
    d = {'A': 0, 'B': 1, 'C': 2}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    e = {'A': 1, 'B': 2, 'C': 0}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    f = {'A': 2, 'B': 0, 'C': 1}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    g = {'A': 1, 'B': 0, 'C': 2}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    h = {'A': 2, 'B': 1, 'C': 0}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    i = {'A': 0, 'B': 2, 'C': 1}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    j = {'A': 0, 'B': 1, 'C': 2}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    k = {'A': 2, 'B': 0, 'C': 1}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    l = {'A': 1, 'B': 2, 'C': 0}
    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    m = {'A': 0, 'B': 2, 'C': 1}
    # 0: A ->

if __name__ == '__main__':
    solve()