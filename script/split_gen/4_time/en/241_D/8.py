def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    for _ in range(Q):
        query = input().rstrip().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            A.sort(reverse=True)
            count = 0
            for a in A:
                if a <= x:
                    count += 1
                    if count == k:
                        print(a)
                        break
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            A.sort()
            count = 0
            for a in A:
                if a >= x:
                    count += 1
                    if count == k:
                        print(a)
                        break
            else:
                print(-1)
