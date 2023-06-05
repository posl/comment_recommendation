def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort()
    sum = 0
    for i in range(len(ab)):
        if ab[i][0] <= m:
            sum += ab[i][1]
            m -= ab[i][0]
        else:
            sum += ab[i][1] * m
            break
    print(sum)
