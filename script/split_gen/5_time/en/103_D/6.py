def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1])
    print(ab)
    count = 0
    for i in range(m-1):
        if ab[i][1] > ab[i+1][0]:
            count += 1
    print(count)
