def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        count = 0
        for j in range(n):
            if x <= a[j]:
                count += 1
        print(count)
