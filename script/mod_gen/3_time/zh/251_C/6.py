def solve():
    N = int(input())
    dic = {}
    for i in range(N):
        s, t = input().split()
        dic[s] = int(t)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic[0][0])

if __name__ == '__main__':
    solve()