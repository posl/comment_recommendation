def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        k -= 1
        l = len(S)
        while t > 0:
            if k < l:
                if S[k] != 'A':
                    if S[k] == 'B':
                        if t % 3 == 1:
                            print('A')
                        elif t % 3 == 2:
                            print('C')
                        else:
                            print('B')
                    else:
                        if t % 3 == 1:
                            print('C')
                        elif t % 3 == 2:
                            print('B')
                        else:
                            print('A')
                    break
            else:
                k = k % l
                if t % 2 == 1:
                    if S[k] == 'A':
                        print('B')
                    elif S[k] == 'B':
                        print('C')
                    else:
                        print('A')
                    break
                else:
                    if S[k] == 'A':
                        print('C')
                    elif S[k] == 'B':
                        print('A')
                    else:
                        print('B')
                    break

if __name__ == '__main__':
    main()