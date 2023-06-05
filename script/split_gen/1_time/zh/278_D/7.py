def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            for i in range(n):
                a[i] = x
        elif query[0] == '2':
            i, x = int(query[1]), int(query[2])
            a[i-1] += x
        else:
            i = int(query[1])
            print(a[i-1])
