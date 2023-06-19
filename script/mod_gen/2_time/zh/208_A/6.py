def dice_sum(A, B):
    for i in range(1, 7):
        for j in range(1, 7):
            if A == 2:
                if i + j == B:
                    return True
            elif A == 3:
                for k in range(1, 7):
                    if i + j + k == B:
                        return True
            elif A == 4:
                for k in range(1, 7):
                    for l in range(1, 7):
                        if i + j + k + l == B:
                            return True
            elif A == 5:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            if i + j + k + l + m == B:
                                return True
            elif A == 6:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                if i + j + k + l + m + n == B:
                                    return True
            elif A == 7:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                for o in range(1, 7):
                                    if i + j + k + l + m + n + o == B:
                                        return True
            elif A == 8:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                for o in range(1, 7):
                                    for p in range(1, 7):
                                        if i + j + k + l + m + n + o + p == B:
                                            return True
            elif A == 9:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                for o in range(1, 7):
                                    for p in

if __name__ == '__main__':
    dice_sum()