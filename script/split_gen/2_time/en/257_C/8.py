def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    # 0以上N未満の整数iについて、W[i]の値がX以上であるようなXの個数を数える
    for i in range(N):
        if S[i] == '1':
            ans += len([x for x in W[i:] if x >= W[i]])
    print(ans)
