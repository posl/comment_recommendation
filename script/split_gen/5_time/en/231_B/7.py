def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.reverse()
    print(s[0])
