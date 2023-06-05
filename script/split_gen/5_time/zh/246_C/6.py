def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([max(0, i - x) for i in a]))
