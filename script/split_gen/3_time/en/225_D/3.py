def main():
    N,Q = map(int,input().split())
    car = [i for i in range(N+1)]
    car[0] = -1
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            car[query[2]] = query[1]
        elif query[0] == 2:
            car[query[2]] = -1
        else:
            ans = []
            ans.append(query[1])
            while car[ans[-1]] != -1:
                ans.append(car[ans[-1]])
            print(len(ans),end=' ')
            print(*ans)
main()
