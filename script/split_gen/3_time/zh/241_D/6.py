def main():
    n = int(input())
    A = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a <= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort(reverse=True)
                print(B[k - 1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a >= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort()
                print(B[k - 1])
