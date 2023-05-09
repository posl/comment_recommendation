def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    
    for i in range(Q):
        count = 0
        for j in range(query[i][0]-1, query[i][1]):
            if A[j] == query[i][2]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()