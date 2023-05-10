def main():
    s = input()
    k = int(input())
    i = 0
    while i < len(s):
        if s[i] != "1":
            break
        i += 1
    if k <= i:
        print(1)
    else:
        print(s[i])
