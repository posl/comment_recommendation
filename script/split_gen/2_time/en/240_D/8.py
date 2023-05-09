def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*N
    for i in range(N):
        b[a[i]-1] += 1
    print(sum(b))
    for i in range(N-1):
        b[a[i]-1] -= 1
        b[a[i+1]-1] += 1
        print(sum(b))
