def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    for i in range(60):
        if N & (1 << i):
            ans.append((1 << i) - 1)
    print(*ans, sep='
')
