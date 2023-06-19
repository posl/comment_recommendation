def main():
    p = list(map(int, input().split()))
    s = []
    for i in range(26):
        s.append(chr(p[i]+96))
    print(''.join(s))
