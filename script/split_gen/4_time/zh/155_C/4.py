def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    max_count = 0
    for i in range(n):
        if s.count(s[i]) > max_count:
            max_count = s.count(s[i])
    for i in range(n):
        if s.count(s[i]) == max_count:
            print(s[i])
