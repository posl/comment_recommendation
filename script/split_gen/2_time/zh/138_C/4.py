def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / ai for ai in a]))
