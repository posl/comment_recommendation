def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        b = list(map(int, input().split()))
        if b[0] == 1:
            a[b[1] - 1] = b[2]
        else:
            print(a[b[1] - 1])
