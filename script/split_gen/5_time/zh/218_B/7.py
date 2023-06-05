def main():
    p = list(map(int, input().split()))
    s = [chr(p[i] + 96) for i in range(26)]
    print(''.join(s))
