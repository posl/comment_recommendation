def main():
    n = int(input())
    data = list(map(int, input().split()))
    print(min_xor(n, data))
