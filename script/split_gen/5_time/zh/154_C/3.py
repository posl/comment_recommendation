def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 5
    A = [2, 6, 1, 4, 5]
    # N = 6
    # A = [4, 1, 3, 1, 6, 2]
    # N = 2
    # A = [10000000, 10000000]
    print('Yes' if len(set(A)) == N else 'No')
