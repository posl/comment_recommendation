def main():
    n = int(input())
    p = []
    for _ in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    sum = 0
    for i in range(1, n):
        sum += p[i]
    sum += p[0] // 2
    print(sum)
