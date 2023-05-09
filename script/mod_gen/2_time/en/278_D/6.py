def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [input().split() for _ in range(q)]
    ans = []
    for query in queries:
        if query[0] == '1':
            a = [int(query[1])] * n
        elif query[0] == '2':
            a[int(query[1]) - 1] += int(query[2])
        else:
            ans.append(a[int(query[1]) - 1])
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()