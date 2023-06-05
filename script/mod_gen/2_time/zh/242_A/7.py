def main():
    n = int(input())
    a = []
    for i in range(n):
        query = input().strip().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x, k = int(query[1]), int(query[2])
            tmp = [i for i in a if i <= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[-k])
        else:
            x, k = int(query[1]), int(query[2])
            tmp = [i for i in a if i >= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[k-1])
main()
