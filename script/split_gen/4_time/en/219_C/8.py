def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: ''.join([chr(96 - ord(c)) for c in x]))
    for i in range(n):
        print(s[i])
