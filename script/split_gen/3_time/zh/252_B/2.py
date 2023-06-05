def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('Yes' if len(set(b) & set(a)) == 0 else 'No')
