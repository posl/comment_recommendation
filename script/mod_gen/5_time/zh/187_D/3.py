def main():
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int,input().split())))
    a_b.sort(key=lambda x:x[0]+x[1],reverse=True)
    a = 0
    b = 0
    for i in range(n):
        a += a_b[i][0]
    for i in range(n):
        b += a_b[i][1]
        a -= a_b[i][0]
        if a < b:
            print(i+1)
            return
    print(n)

if __name__ == '__main__':
    main()