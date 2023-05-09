def main():
    N = int(input())
    ans = 0
    while 2**ans <= N:
        ans += 1
    print(ans-1)
