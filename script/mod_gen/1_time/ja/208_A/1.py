def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == B and A == 2:
                print("Yes")
                return
            for k in range(1, 7):
                if i + j + k == B and A == 3:
                    print("Yes")
                    return
                for l in range(1, 7):
                    if i + j + k + l == B and A == 4:
                        print("Yes")
                        return
                    for m in range(1, 7):
                        if i + j + k + l + m == B and A == 5:
                            print("Yes")
                            return
                        for n in range(1, 7):
                            if i + j + k + l + m + n == B and A == 6:
                                print("Yes")
                                return
    print("No")
    return

if __name__ == '__main__':
    main()