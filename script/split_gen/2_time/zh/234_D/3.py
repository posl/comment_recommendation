def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # print(n, k, p)
    # print(p[0:3])
    # print(p[0:2])
    # print(p[0:1])
    # print(p[0:0])
    for i in range(k-1,n):
        print(max(p[i-k+1:i+1]))
