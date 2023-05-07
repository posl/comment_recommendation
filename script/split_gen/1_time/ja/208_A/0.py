def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == B and A == 2:
                print('Yes')
                return
            for k in range(1, 7):
                if i + j + k == B and A == 3:
                    print('Yes')
                    return
                for l in range(1, 7):
                    if i + j + k + l == B and A == 4:
                        print('Yes')
                        return
                    for m in range(1, 7):
                        if i + j + k + l + m == B and A == 5:
                            print('Yes')
                            return
                        for n in range(1, 7):
                            if i + j + k + l + m + n == B and A == 6:
                                print('Yes')
                                return
                            for o in range(1, 7):
                                if i + j + k + l + m + n + o == B and A == 7:
                                    print('Yes')
                                    return
                                for p in range(1, 7):
                                    if i + j + k + l + m + n + o + p == B and A == 8:
                                        print('Yes')
                                        return
                                    for q in range(1, 7):
                                        if i + j + k + l + m + n + o + p + q == B and A == 9:
                                            print('Yes')
                                            return
                                        for r in range(1, 7):
                                            if i + j + k + l + m + n + o + p + q + r == B and A == 10:
                                                print('Yes')
                                                return
                                            for s in range(1, 7):
                                                if i + j + k + l + m + n + o + p + q + r + s == B and A == 11:
                                                    print('Yes')
                                                    return
                                                for t in range(1, 7):
                                                    if i + j + k + l + m + n + o + p + q + r + s + t == B and A == 12:
                                                        print('Yes')
                                                        return
                                                    for u in range(1, 7):
                                                        if
