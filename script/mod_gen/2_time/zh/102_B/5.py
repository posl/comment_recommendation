def max_abs_diff():
    N = int(input())
    A = list(map(int, input().split()))
    max_A = max(A)
    min_A = min(A)
    print(max_A - min_A)

if __name__ == '__main__':
    max_abs_diff()