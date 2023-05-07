def main():
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c = query[2]
            print("insert", x, c)
        elif query[0] == 2:
            c = query[1]
            print("take", c)
        else:
            print("error")
            return
