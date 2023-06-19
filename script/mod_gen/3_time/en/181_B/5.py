def main():
    N = int(input())
    total = 0
    for i in range(N):
        A, B = map(int, input().split())
        total += (B - A + 1) * (A + B) // 2
    print(total % 1000000007)
main()
