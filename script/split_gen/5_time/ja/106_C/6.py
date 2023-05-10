def main():
    s = input()
    k = int(input())
    i = 0
    while i < len(s) and s[i] == '1':
        i += 1
    if i >= k:
        print(1)
    else:
        print(s[i])
