def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    sum = 0
    for i in range(N):
        if i == 0:
            sum += p[i] // 2
        else:
            sum += p[i]
    print(sum)
