def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + p[i] - 1) for i in range(len(p))]
    print(''.join(s))
