def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            a[l[1] - 1] = l[2]
        else:
            print(a[l[1] - 1])
