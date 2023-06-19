def main():
    n,k = map(int,input().split())
    s = input()
    
    # 从左到右计数
    left = [0] * (n+1)
    for i in range(n):
        left[i+1] = left[i] + (s[i] == '0')
    # 从右到左计数
    right = [0] * (n+1)
    for i in range(n-1,-1,-1):
        right[i] = right[i+1] + (s[i] == '1')
    
    ans = 0
    # 选择左端点
    for i in range(n+1):
        # 选择右端点
        j = min(n,i+k*2)
        # 选择左端点为i，右端点为j时，最多能有多少个人
        ans = max(ans,left[i] + right[j])
    
    print(ans)
