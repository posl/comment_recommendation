def main():
    s1 = list(input())
    s2 = list(input())
    s3 = list(input())
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    for p in permutations(range(10), len(chars)):
        d = {chars[i]: p[i] for i in range(len(chars))}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int("".join([str(d[c]) for c in s1]))
        n2 = int("".join([str(d[c]) for c in s2]))
        n3 = int("".join([str(d[c]) for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

if __name__ == '__main__':
    main()