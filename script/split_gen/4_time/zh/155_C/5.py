def main():
    n = int(input())
    s = [input() for _ in range(n)]
    max_count = 0
    for i in range(n):
        if s.count(s[i]) > max_count:
            max_count = s.count(s[i])
    max_s = []
    for i in range(n):
        if s.count(s[i]) == max_count and s[i] not in max_s:
            max_s.append(s[i])
    max_s.sort()
    for i in max_s:
        print(i)
