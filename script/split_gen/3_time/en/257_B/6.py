def main():
    n,k,q = map(int, input().split())
    a = [0] * n
    for i in map(int, input().split()):
        a[i-1] += 1
    for i in range(q):
        l = int(input())
        print(k - a[l-1])
