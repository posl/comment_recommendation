def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans = (ans + a) % 360
    print(min(ans, 360-ans))
main()
