def main():
    q = int(input())
    A = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            num = 0
            for a in A:
                if a <= x:
                    num += 1
            if num < k:
                print(-1)
            else:
                B = A.copy()
                B.sort(reverse=True)
                print(B[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            num = 0
            for a in A:
                if a >= x:
                    num += 1
            if num < k:
                print(-1)
            else:
                B = A.copy()
                B.sort()
                print(B[k-1])
