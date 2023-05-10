def main():
    N = int(input())
    p = list(map(int, input().split()))
    for i in range(N):
        p[i] -= 1
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    if count == N:
        print(N)
        exit()
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    print(count)
