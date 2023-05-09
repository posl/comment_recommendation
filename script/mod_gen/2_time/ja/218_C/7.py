def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(input()))
    for i in range(N):
        T.append(list(input()))
    # S,Tを90度回転させる
    S90 = [list(i) for i in zip(*S[::-1])]
    # S,Tを180度回転させる
    S180 = [list(i) for i in zip(*S90[::-1])]
    # S,Tを270度回転させる
    S270 = [list(i) for i in zip(*S180[::-1])]
    # S,Tを平行移動させる
    for i in range(N):
        for j in range(N):
            # S,Tを90度回転させる
            if S90 == T:
                print("Yes")
                return
            # S,Tを180度回転させる
            elif S180 == T:
                print("Yes")
                return
            # S,Tを270度回転させる
            elif S270 == T:
                print("Yes")
                return
            else:
                # S,Tを90度回転させる
                S90 = [list(i) for i in zip(*S90[::-1])]
                # S,Tを180度回転させる
                S180 = [list(i) for i in zip(*S180[::-1])]
                # S,Tを270度回転させる
                S270 = [list(i) for i in zip(*S270[::-1])]
        # S,Tを平行移動させる
        S90 = [list(i) for i in zip(*S90)]
        S180 = [list(i) for i in zip(*S180)]
        S270 = [list(i) for i in zip(*S270)]
    print("No")
main()

if __name__ == '__main__':
    main()