def main():
    p = list(map(int, input().split()))
    s = [chr(96 + i) for i in p]
    print(''.join(s))
