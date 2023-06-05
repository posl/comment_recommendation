def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        b, c = map(int, input().split())
        sum += (c - b) * a.count(b)
        print(sum)
        a = [c if x == b else x for x in a]
