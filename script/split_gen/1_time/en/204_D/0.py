def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) // 2)
main()
