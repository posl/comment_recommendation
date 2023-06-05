def main():
    n,q = map(int,input().split())
    l = [i for i in range(n+1)]
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            l[query[1]],l[query[2]] = l[query[2]],l[query[1]]
        elif query[0] == 2:
            l[query[1]],l[query[2]] = l[query[2]],l[query[1]]
        else:
            ans = []
            for i in range(n+1):
                if l[i] == l[query[1]]:
                    ans.append(i)
            print(len(ans),*ans)

if __name__ == '__main__':
    main()