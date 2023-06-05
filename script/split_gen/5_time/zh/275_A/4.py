def main():
    num = int(input())
    height = list(map(int, input().split()))
    print(height.index(max(height)) + 1)
