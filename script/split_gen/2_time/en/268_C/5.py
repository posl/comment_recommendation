def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i:
            if i == n-1:
                p[i], p[0] = p[0], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
            count += 1
    print(count)
