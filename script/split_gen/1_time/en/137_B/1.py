def main():
    k, x = map(int, input().split())
    start = x - k + 1
    end = x + k - 1
    for i in range(start, end + 1):
        print(i, end=' ')
