def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_a = max(A)
    min_a = min(A)
    if max_a == min_a:
        print(-1)
        return
    if min_a == 0:
        print(max_a)
        return
    print(max_a * 2)

if __name__ == '__main__':
    main()