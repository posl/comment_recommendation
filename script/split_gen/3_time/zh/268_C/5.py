def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count)
