def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N == 2:
        if M == 0:
            print("1 2")
        else:
            print("-1")
    else:
        if M == 0:
            print("1 2 3")
        else:
            if M == 1:
                if A[0] == 1:
                    print("-1")
                else:
                    print("1 2 3")
            else:
                if A[0] == 1:
                    print("-1")
                else:
                    if A[1] == 1:
                        print("-1")
                    else:
                        print("1 2 3")
main()

if __name__ == '__main__':
    main()