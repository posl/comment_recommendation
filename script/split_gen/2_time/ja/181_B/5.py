def main():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    
    ans = 0
    for i in range(N):
        ans += (AB[i][1] - AB[i][0] + 1) * (AB[i][0] + AB[i][1]) // 2
    
    print(ans % 1000000007)
