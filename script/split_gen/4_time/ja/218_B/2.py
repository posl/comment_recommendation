def main():
    p = list(map(int, input().split()))
    a = [chr(ord('a') + i - 1) for i in p]
    print(''.join(a))
