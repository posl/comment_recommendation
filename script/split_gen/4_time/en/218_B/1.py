def main():
    p = list(map(int, input().split()))
    s = ""
    for i in range(26):
        s += chr(p.index(i + 1) + 97)
    print(s)
