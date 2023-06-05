def main():
    p = list(map(int, input().split()))
    s = ''
    for i in p:
        s += chr(ord('a') + i - 1)
    print(s)
