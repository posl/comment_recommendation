def main():
    n = int(input())
    hs = list(map(int, input().split()))
    for i in range(n - 1):
        if hs[i + 1] - hs[i] > 1:
            print('No')
            return
        elif hs[i + 1] - hs[i] == 1:
            hs[i + 1] -= 1
    print('Yes')
