def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    print('Yes' if is_possible(N, x, y, A) else 'No')
