def main():
    from itertools import permutations
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    for p in permutations(range(10), len(chars)):
        d = {c: p[i] for i, c in enumerate(chars)}
        n1 = int("".join([str(d[c]) for c in s1]))
        n2 = int("".join([str(d[c]) for c in s2]))
        n3 = int("".join([str(d[c]) for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
main()

if __name__ == '__main__':
    main()