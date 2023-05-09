def main():
    p = list(map(int, input().split()))
    p = [chr(ord('a') + i - 1) for i in p]
    print(''.join(p))
