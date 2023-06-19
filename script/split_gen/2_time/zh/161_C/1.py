def main():
    n, k = map(int, input().split())
    print(n%k if n%k < k else k - n%k)
