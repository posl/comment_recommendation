def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [1 / i for i in a]
    print(1 / sum(b))
