def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [0 for i in range(n)]
    for i in range(n):
        q[p[i]-1] = i+1
    print(' '.join([str(i) for i in q]))
