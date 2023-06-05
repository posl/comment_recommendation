def main():
    n,m = map(int,input().split())
    b = []
    for i in range(n):
        b.append(list(map(int,input().split())))
    for i in range(10**100):
        for j in range(7):
            a = i*7 + j + 1
            if a == b[0][0]:
                for k in range(n):
                    for l in range(m):
                        if i+k*7 + l + 1 != b[k][l]:
                            break
                    if i+k*7 + l + 1 != b[k][l]:
                        break
                else:
                    print("Yes")
                    exit()
    else:
        print("No")
        exit()

if __name__ == '__main__':
    main()