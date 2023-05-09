def main():
    p = list(map(int, input().split()))
    for i in range(26):
        print(chr(p[i]+96), end="")
    print()
