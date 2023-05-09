def main():
    n = int(input())
    aoki = 0
    takahashi = 0
    for i in range(n):
        a, t = map(int, input().split())
        aoki += a
        takahashi += t
    if aoki > takahashi:
        print(0)
    else:
        print(1)
