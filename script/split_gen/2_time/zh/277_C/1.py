def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    print(ab)
    m = 0
    for i in range(n):
        if ab[i][0] > m:
            print(ab[i][0])
            return
        m = max(m, ab[i][1])
    print(m)
