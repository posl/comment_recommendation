def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(sum(h) - n)
