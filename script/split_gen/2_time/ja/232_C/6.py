def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    cd = [tuple(map(int, input().split())) for _ in range(m)]
    for p in permutations(range(1, n + 1)):
        if all(ab[i] in zip(p, p) or ab[i] in zip(p, p[::-1]) for i in range(m)) and all(cd[i] in zip(p, p) or cd[i] in zip(p, p[::-1]) for i in range(m)):
            print('Yes')
            break
    else:
        print('No')
