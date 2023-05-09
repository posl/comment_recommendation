def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        if b[i][0] == 1:
            a = [b[i][1]] * n
        elif b[i][0] == 2:
            a[b[i][1] - 1] += b[i][2]
        else:
            print(a[b[i][1] - 1])
