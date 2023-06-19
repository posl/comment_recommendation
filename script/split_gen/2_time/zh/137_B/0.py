def main():
    k, x = map(int, input().split())
    print(' '.join(map(str, [x - k + 1, x + k - 1])))
