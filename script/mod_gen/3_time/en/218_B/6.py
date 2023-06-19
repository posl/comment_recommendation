def main():
    p = list(map(int,input().split()))
    s = ""
    for i in range(26):
        s += chr(ord('a') + p[i] - 1)
    print(s)
main()
