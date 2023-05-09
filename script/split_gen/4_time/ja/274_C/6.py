def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = [0]*(2*n+1)
    p[1] = 1
    for i in range(n):
        p[2*i+2] = p[i+1]
        p[2*i+3] = p[i+1]
    for i in range(2*n+1):
        print(p[i+1])
