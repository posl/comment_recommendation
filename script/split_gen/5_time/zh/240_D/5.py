def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        b.append(0)
    for i in range(N):
        b[a[i] - 1] += 1
    for i in range(N):
        print(N - b[a[i] - 1] + 1)
