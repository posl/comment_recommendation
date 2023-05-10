def main():
    p = list(map(int, input().split()))
    s = [None] * 26
    for i in range(26):
        s[p[i]-1] = chr(97+i)
    print("".join(s))
