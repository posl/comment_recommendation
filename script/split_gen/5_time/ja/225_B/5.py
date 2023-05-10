def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    ab.sort()
    count = 0
    for i in range(n-1):
        if ab[i][1] == n:
            count += 1
    if count == n-1:
        print('Yes')
    else:
        print('No')
