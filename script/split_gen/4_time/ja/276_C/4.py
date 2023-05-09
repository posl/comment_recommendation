def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = []
    for i in range(n):
        q.append(0)
    for i in range(n):
        q[p[i]-1] = i+1
    print(" ".join(map(str,q)))
