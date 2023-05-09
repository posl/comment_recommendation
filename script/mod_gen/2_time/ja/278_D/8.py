def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    query = [list(map(int,input().split())) for i in range(q)]
    x = 0
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            x = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
            a[query[i][1]-1] -= x
        else:
            ans.append(a[query[i][1]-1] + x)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()