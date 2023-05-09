def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [input().split() for _ in range(q)]
    ans = []
    add = 0
    for query in queries:
        if query[0] == '1':
            add = int(query[1])
        elif query[0] == '2':
            a[int(query[1])-1] += int(query[2])
        else:
            ans.append(a[int(query[1])-1] + add)
    print(*ans, sep='
')
main()

if __name__ == '__main__':
    main()