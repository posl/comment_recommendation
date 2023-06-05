def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x_dict = {}
    for i in range(26):
        x_dict[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = ''.join([x_dict[x] for x in s[i]])
    s.sort()
    for i in range(n):
        print(s[i])
