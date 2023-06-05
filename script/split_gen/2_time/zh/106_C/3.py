def main():
    s = input()
    k = int(input())
    i = 0
    while i < k:
        if s[i] == '1':
            i += 1
        else:
            break
    print(s[i])
