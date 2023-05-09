def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*(N+1)
    for i in range(N):
        b[i+1] = b[i] + a[i]
    c = []
    for i in range(N):
        for j in range(i+1, N+1):
            c.append((b[j] - b[i])//(j-i))
    c.sort()
    print(c[(len(c)-1)//2])
