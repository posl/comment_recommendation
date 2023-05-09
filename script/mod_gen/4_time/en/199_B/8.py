def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max_a = max(A)
    min_b = min(B)
    if min_b < max_a:
        print(0)
    else:
        print(min_b - max_a + 1)

if __name__ == '__main__':
    main()