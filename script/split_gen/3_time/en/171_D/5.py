def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    b = [0]*q
    c = [0]*q
    for i in range(q):
        b[i],c[i] = map(int,input().split())
    for i in range(q):
        for j in range(n):
            if a[j] == b[i]:
                a[j] = c[i]
    print(sum(a))
