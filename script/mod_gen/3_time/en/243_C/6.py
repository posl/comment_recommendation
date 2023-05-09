def main():
    n = int(input())
    x = []
    y = []
    s = input()
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    if n == 2:
        if s[0] == s[1]:
            print("No")
        else:
            if x[0] == x[1]:
                print("Yes")
            else:
                print("No")
    else:
        if s[0] == s[1]:
            print("No")
        else:
            if x[0] == x[1]:
                print("Yes")
            else:
                if x[0] == x[2]:
                    print("Yes")
                else:
                    if x[1] == x[2]:
                        print("Yes")
                    else:
                        if x[0] < x[1]:
                            if x[0] < x[2]:
                                if x[1] < x[2]:
                                    print("No")
                                else:
                                    print("Yes")
                            else:
                                print("Yes")
                        else:
                            if x[0] < x[2]:
                                print("Yes")
                            else:
                                if x[1] < x[2]:
                                    print("Yes")
                                else:
                                    print("No")

if __name__ == '__main__':
    main()