def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print('Yes' if sum(a) - (len(a)//2) <= x else 'No')
