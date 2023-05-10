def solve():
    n = input()
    if '0' in n:
        return -1
    if len(n) == 1:
        if int(n) % 3 == 0:
            return 0
        else:
            return -1
    n = list(map(int, n))
    n.sort(reverse=True)
    sum_n = sum(n)
    if sum_n % 3 == 0:
        return 0
    else:
        if sum_n % 3 == 1:
            if 1 in n:
                n.remove(1)
                if sum(n) % 3 == 0:
                    return 1
                else:
                    if 2 in n:
                        n.remove(2)
                        if sum(n) % 3 == 0:
                            return 2
                        else:
                            return -1
                    else:
                        return -1
            else:
                if 4 in n:
                    n.remove(4)
                    if sum(n) % 3 == 0:
                        return 1
                    else:
                        return -1
                else:
                    return -1
        else:
            if 2 in n:
                n.remove(2)
                if sum(n) % 3 == 0:
                    return 1
                else:
                    if 1 in n:
                        n.remove(1)
                        if sum(n) % 3 == 0:
                            return 2
                        else:
                            return -1
                    else:
                        return -1
            else:
                if 5 in n:
                    n.remove(5)
                    if sum(n) % 3 == 0:
                        return 1
                    else:
                        return -1
                else:
                    return -1
print(solve())

if __name__ == '__main__':
    solve()