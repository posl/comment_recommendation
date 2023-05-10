def main():
    p = list(map(int, input().split()))
    alphabets = [chr(ord('a') + i - 1) for i in p]
    print(''.join(alphabets))
