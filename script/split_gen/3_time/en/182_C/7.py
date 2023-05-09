def main():
    N = input()
    k = len(N)
    N = list(map(int, N))
    mod = sum(N) % 3
    if mod == 0:
        return 0
    else:
        if k == 1:
            return -1
        elif k == 2:
            if mod == 1:
                return -1
            else:
                return 1
        else:
            if mod == 1:
                if 1 in N:
                    return 1
                elif 4 in N:
                    return 1
                elif 7 in N:
                    return 1
                else:
                    if 2 in N:
                        return 2
                    elif 5 in N:
                        return 2
                    elif 8 in N:
                        return 2
                    else:
                        return -1
            else:
                if 2 in N:
                    return 1
                elif 5 in N:
                    return 1
                elif 8 in N:
                    return 1
                else:
                    if 1 in N:
                        return 2
                    elif 4 in N:
                        return 2
                    elif 7 in N:
                        return 2
                    else:
                        return -1
