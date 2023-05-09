def main():
    N = int(input())
    vs = sorted(list(map(int, input().split())))
    ans = vs[0]
    for i in range(1, N):
        ans = (ans + vs[i]) / 2
    print(ans)
main()
from sys import stdin, stdout
