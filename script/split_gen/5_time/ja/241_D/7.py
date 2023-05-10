def main():
    n = int(input())
    a = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x,k = int(query[1]),int(query[2])
            a.sort()
            if a.count(x) < k:
                print(-1)
            else:
                print(a[-k])
        elif query[0] == '3':
            x,k = int(query[1]),int(query[2])
            a.sort()
            if a.count(x) < k:
                print(-1)
            else:
                print(a[k-1])
