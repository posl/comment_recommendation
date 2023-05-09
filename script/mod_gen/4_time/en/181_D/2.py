def main():
    S = input()
    if len(S) == 1:
        if int(S) == 8:
            print("Yes")
            return
        else:
            print("No")
            return
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[1] + S[0]) % 8 == 0:
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        S = list(S)
        S.sort()
        S = "".join(S)
        for i in range(112,1000,8):
            if len(str(i)) < 3:
                continue
            else:
                if len(set(str(i))) == 3:
                    continue
                else:
                    if int(S) % i == 0:
                        print("Yes")
                        return
        print("No")
        return

if __name__ == '__main__':
    main()