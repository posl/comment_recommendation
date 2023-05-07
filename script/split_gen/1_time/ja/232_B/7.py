def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for k in range(1, 26):
            if s == ''.join([chr((ord(c) - ord('a') + k) % 26 + ord('a')) for c in t]):
                print('Yes')
                return
        print('No')
