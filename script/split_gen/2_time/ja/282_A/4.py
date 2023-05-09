def main():
    n = int(input())
    ans = ''
    for i in range(n):
        ans += chr(ord('A') + i)
    print(ans)
