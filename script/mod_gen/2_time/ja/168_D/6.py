def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        edge[A - 1].append(B - 1)
        edge[B - 1].append(A - 1)
    print("Yes")
    for i in range(1, N):
        print(edge[i][0] + 1)
main()
上記のコードでWAが出ました。なぜかわかりません。
最初の行を追加してみたらACでした。
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    main()