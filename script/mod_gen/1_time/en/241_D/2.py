def main():
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            k = query[2]
            if k > len(A):
                ans.append(-1)
            else:
                ans.append(A[-k])
        elif query[0] == 3:
            A.sort()
            k = query[2]
            if k > len(A):
                ans.append(-1)
            else:
                ans.append(A[k-1])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()