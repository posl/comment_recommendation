def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l,r,x = map(int, input().split())
        count = 0
        for j in range(l-1,r):
            if a[j] == x:
                count += 1
        print(count)
