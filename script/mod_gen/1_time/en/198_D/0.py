def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    if n1 < n2:
        s1, s2 = s2, s1
        n1, n2 = n2, n1
    if n1 < n3:
        s1, s3 = s3, s1
        n1, n3 = n3, n1
    if n2 < n3:
        s2, s3 = s3, s2
        n2, n3 = n3, n2
    if n1 == n2 and n1 == n3:
        if s1 == s2 and s1 == s3:
            if s1 == 'a':
                print(1)
                print(1)
                print(1)
                return
            else:
                print('UNSOLVABLE')
                return
        else:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        if i + j == k and s1[0] != str(i) and s2[0] != str(j) and s3[0] != str(k):
                            print(i)
                            print(j)
                            print(k)
                            return
    elif n1 == n2 and n1 > n3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if s1[0] != str(i) and s2[0] != str(j) and s3[0] != str(k):
                        if s1[-n3:] == s3:
                            if s2[-n3:] == s3:
                                if i + j == k:
                                    print(i)
                                    print(j)
                                    print(k)
                                    return
                            else:
                                if i + j == k:
                                    print(i)
                                    print(j)
                                    print(k)
                                    return
                                else:
                                    if i + j + 1 == k:
                                        print(i)
                                        print(j)
                                        print(k)
                                        return
        print('UNSOLVABLE')
        return
    elif n1 == n2 and n1 < n3:
        for i in range(10):
            for j

if __name__ == '__main__':
    solve()