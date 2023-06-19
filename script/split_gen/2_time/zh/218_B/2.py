def main():
    p = list(map(int, input().split()))
    p = [chr(ord('a') + x - 1) for x in p]
    print(''.join(p))
