def main():
    n = int(input())
    v = list(map(int, input().split()))
    print(min(replace(v, 0), replace(v, 1)))
