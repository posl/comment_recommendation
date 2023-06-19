def main():
    n = int(input())
    s = {}
    for i in range(n):
        name = input()
        if name in s:
            s[name] += 1
        else:
            s[name] = 1
    print(max(s, key=s.get))
