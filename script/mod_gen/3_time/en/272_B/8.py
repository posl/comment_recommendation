def main():
    N, M = map(int, input().split())
    for i in range(M):
        k, *x = map(int, input().split())
        if k == 1:
            if len(x) != 1:
                print("No")
                return
        elif k == 2:
            if x[0] == x[1]:
                print("No")
                return
        else:
            if x[0] == x[1] or x[1] == x[2]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()