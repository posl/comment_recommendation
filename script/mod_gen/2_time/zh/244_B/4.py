def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if t[i-1] == 'R' and t[i-2] == 'R':
                if t[i-3] == 'R':
                    if t[i-4] == 'R':
                        if t[i-5] == 'R':
                            if t[i-6] == 'R':
                                if t[i-7] == 'R':
                                    if t[i-8] == 'R':
                                        if t[i-9] == 'R':
                                            if t[i-10] == 'R':
                                                if t[i-11] == 'R':
                                                    if t[i-12] == 'R':
                                                        if t[i-13] == 'R':
                                                            if t[i-14] == 'R':
                                                                if t[i-15] == 'R':
                                                                    if t[i-16] == 'R':
                                                                        if t[i-17] == 'R':
                                                                            if t[i-18] == 'R':
                                                                                if t[i-19] == 'R':
                                                                                    if t[i-20] == 'R':
                                                                                        y -= 1
                                                                                    else:
                                                                                        x += 1
                                                                                else:
                                                                                    y -= 1
                                                                            else:
                                                                                x -= 1
                                                                        else:
                                                                            y += 1
                                                                    else:
                                                                        x += 1
                                                                else:
                                                                    y -= 1
                                                            else:
                                                                x -= 1
                                                        else:
                                                            y += 1
                                                    else:
                                                        x += 1
                                                else:
                                                    y -= 1
                                            else:
                                                x -= 1
                                        else:
                                            y += 1
                                    else:
                                        x += 1
                                else:
                                    y -= 1
                            else:
                                x -= 1
                        else:
                            y += 1
                    else:
                        x += 1
                else:
                    y -= 1
            else:
                x += 1
        else:
            if t[i-1] == 'R' and t[i-2] == 'R':
                if t[i-3] == 'R':
                    if t[i-4] == 'R':
                        if t[i-5] == 'R':
                            if t[i-6

if __name__ == '__main__':
    main()