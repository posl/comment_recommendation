def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    x = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
        elif query[0] == 2:
            a[query[1] - 1] += query[2] - x
        else:
            print(a[query[1] - 1] + x)
