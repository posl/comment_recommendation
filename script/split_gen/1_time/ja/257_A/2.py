def main():
    N, X = map(int, input().split())
    alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    ans = ''
    for i in range(N):
        ans += alphabet[(X-1)//N]
    print(ans)
