def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 最大公约数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    # 最小公倍数
    def lcm(a, b):
        return a * b // gcd(a, b)
    # 最小公倍数
    ans = A[0]
    for i in range(1, N):
        ans = lcm(ans, A[i])
    
    print(ans)
