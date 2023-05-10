def main():
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append(s.split())
    l.sort()
    ans = []
    ans.append(l[0])
    for i in range(1,n):
        if int(l[i][0]) >= int(ans[-1][1]):
            ans.append(l[i])
        elif int(l[i][1]) > int(ans[-1][1]):
            ans[-1][1] = l[i][1]
    for i in ans:
        print(i[0],i[1])

if __name__ == '__main__':
    main()