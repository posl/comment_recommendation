def main():
    S = input()
    Q = int(input())
    # 0: original, 1: reversed
    rev = 0
    # 0: original, 1: reversed
    front = []
    back = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            rev = 1 - rev
        else:
            if query[1] == '1':
                if rev == 0:
                    front.append(query[2])
                else:
                    back.append(query[2])
            else:
                if rev == 0:
                    back.append(query[2])
                else:
                    front.append(query[2])
    if rev == 0:
        print(''.join(front[::-1]) + S + ''.join(back))
    else:
        print(''.join(back[::-1]) + S[::-1] + ''.join(front))

if __name__ == '__main__':
    main()