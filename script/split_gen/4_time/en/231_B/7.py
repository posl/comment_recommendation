def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s = s[::-1]
    print(s[0])
