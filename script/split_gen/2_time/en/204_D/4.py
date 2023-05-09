def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(sum(t) - max(t) // 2)
