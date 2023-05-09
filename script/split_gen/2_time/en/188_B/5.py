def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('Yes' if sum([a[i] * b[i] for i in range(n)]) == 0 else 'No')
