def max_diff():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

if __name__ == '__main__':
    max_diff()