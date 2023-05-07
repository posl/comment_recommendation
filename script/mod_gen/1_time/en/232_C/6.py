def main():
    n, m = map(int, input().split())
    aoki = []
    taka = []
    for i in range(m):
        aoki.append(list(map(int, input().split())))
    for i in range(m):
        taka.append(list(map(int, input().split())))
    if m == 0:
        print("Yes")
        return
    for i in range(m):
        if aoki[i][0] != taka[i][0]:
            break
        if i == m-1:
            print("Yes")
            return
    for i in range(m):
        if aoki[i][1] != taka[i][1]:
            break
        if i == m-1:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()