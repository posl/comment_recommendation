def main():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        idx = bisect.bisect_left(a,x[i])
        print(n-idx)