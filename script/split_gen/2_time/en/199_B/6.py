def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for i in range(1, 1001):
        if min(b) < i or max(a) > i:
            continue
        ans += 1
        
    print(ans)
