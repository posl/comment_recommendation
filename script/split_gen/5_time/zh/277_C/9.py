def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab = sorted(ab, key=lambda x: x[1])
    cur = 0
    for i in range(n):
        if cur < ab[i][0]:
            cur = ab[i][1]
    print(cur)
