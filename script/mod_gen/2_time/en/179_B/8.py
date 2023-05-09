def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n-2):
        if l[i][0] == l[i][1] == l[i+1][0] == l[i+1][1] == l[i+2][0] == l[i+2][1]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()