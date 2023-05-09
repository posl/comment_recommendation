def solve(s1, s2, s3):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if s1[0] == s2[0] and s2[0] == s3[0] and i == j == k:
                    continue
                if s1[0] != s2[0] and s2[0] == s3[0] and i != j == k:
                    continue
                if s1[0] == s2[0] and s2[0] != s3[0] and i == j != k:
                    continue
                if s1[0] != s2[0] and s2[0] != s3[0] and i != j != k:
                    continue
                if s1[0] == s3[0] and s2[0] == s3[0] and i == k == j:
                    continue
                if s1[0] != s3[0] and s2[0] == s3[0] and i != k == j:
                    continue
                if s1[0] == s3[0] and s2[0] != s3[0] and i == k != j:
                    continue
                if s1[0] != s3[0] and s2[0] != s3[0] and i != k != j:
                    continue
                n1 = i
                n2 = j
                n3 = k
                for c1, c2, c3 in zip(s1[1:], s2[1:], s3[1:]):
                    if c1 == c2 == c3:
                        n1 = n1 * 10
                        n2 = n2 * 10
                        n3 = n3 * 10
                    elif c1 != c2 == c3:
                        n1 = n1 * 10
                        n2 = n2 * 10
                        n3 = n3 * 10 + 1
                    elif c1 == c2 != c3:
                        n1 = n1 * 10
                        n2 = n2 * 10 + 1
                        n3 = n3 * 10
                    elif c1 != c2 != c3:
