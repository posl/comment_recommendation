def main():
    S = input()
    if len(S) == 1:
        if int(S) % 8 == 0:
            print("Yes")
        else:
            print("No")
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        s = [0] * 10
        for i in S:
            s[int(i)] += 1
        for i in range(100, 1000, 8):
            t = s[:]
            for j in str(i):
                t[int(j)] -= 1
                if t[int(j)] < 0:
                    break
            else:
                print("Yes")
                break
        else:
            print("No")

if __name__ == '__main__':
    main()