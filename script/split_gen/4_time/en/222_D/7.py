def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = 0
    for i in range(n):
        result += (b[i] - a[i] + 1)
        
    print(result % 998244353)
