def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    ans = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a = [query[1]]*n
        elif query[0] == 2:
            a[query[1]-1] += query[2]
        else:
            ans.append(a[query[1]-1])
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()