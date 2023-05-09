def main():
    S = input()
    x = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if S[0] == 'o':
                        if i != 0:
                            continue
                    elif S[0] == 'x':
                        if i == 0:
                            continue
                    if S[1] == 'o':
                        if j != 1:
                            continue
                    elif S[1] == 'x':
                        if j == 1:
                            continue
                    if S[2] == 'o':
                        if k != 2:
                            continue
                    elif S[2] == 'x':
                        if k == 2:
                            continue
                    if S[3] == 'o':
                        if l != 3:
                            continue
                    elif S[3] == 'x':
                        if l == 3:
                            continue
                    if S[4] == 'o':
                        if i != 4:
                            continue
                    elif S[4] == 'x':
                        if i == 4:
                            continue
                    if S[5] == 'o':
                        if j != 5:
                            continue
                    elif S[5] == 'x':
                        if j == 5:
                            continue
                    if S[6] == 'o':
                        if k != 6:
                            continue
                    elif S[6] == 'x':
                        if k == 6:
                            continue
                    if S[7] == 'o':
                        if l != 7:
                            continue
                    elif S[7] == 'x':
                        if l == 7:
                            continue
                    if S[8] == 'o':
                        if i != 8:
                            continue
                    elif S[8] == 'x':
                        if i == 8:
                            continue
                    if S[9] == 'o':
                        if j != 9:
                            continue
                    elif S[9] == 'x':
                        if j == 9:
                            continue
                    x += 1
    print(x)

if __name__ == '__main__':
    main()