def solve():
    # === 数値の入力 ===
    #n = int(input())
    #a, b = map(int, input().split())
    #m = [list(map(int,input().split())) for i in range(n)]
    #a = list(map(int,input().split()))
    s = input()
    t = input()
    # === 問題解答 ===
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")
    #for i in range(n):
    #    print(a[i])
    #print(" ".join(map(str, a)))
    #print("".join(map(str, a)))

if __name__ == '__main__':
    solve()