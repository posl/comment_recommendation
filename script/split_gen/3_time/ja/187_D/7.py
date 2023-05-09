def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = sum([ab[i][0] for i in range(n)])
    takahashi = 0
    for i in range(n):
        aoki -= ab[i][0]
        takahashi += ab[i][0] + ab[i][1]
        if takahashi > aoki:
            print(i+1)
            break
