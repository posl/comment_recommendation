def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        else:
            x,k = query[1],query[2]
            if query[0] == 2:
                A.sort(reverse=True)
                ans = -1
                count = 0
                for i in A:
                    if i <= x:
                        count += 1
                        if count == k:
                            ans = i
                            break
            else:
                A.sort()
                ans = -1
                count = 0
                for i in A:
                    if i >= x:
                        count += 1
                        if count == k:
                            ans = i
                            break
            if ans != -1:
                print(ans)

if __name__ == '__main__':
    main()