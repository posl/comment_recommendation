def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    for i in range(q):
        l, r, x = [int(x) for x in input().split()]
        print(a[l-1:r].count(x))
