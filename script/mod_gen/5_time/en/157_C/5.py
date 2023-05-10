def main():
    n,m = map(int, input().split())
    sc = []
    for i in range(m):
        s,c = map(int, input().split())
        sc.append([s,c])
    sc.sort(key=lambda x: x[0])
    ans = -1
    for i in range(10**(n-1), 10**n):
        i = str(i)
        if len(i) != n:
            continue
        for j in range(m):
            if i[sc[j][0]-1] != str(sc[j][1]):
                break
        else:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()