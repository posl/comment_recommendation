def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort()
    s_count = {}
    for i in range(n):
        if s[i] in s_count:
            s_count[s[i]] += 1
        else:
            s_count[s[i]] = 1
    max_key = max(s_count, key=s_count.get)
    for k, v in s_count.items():
        if v == s_count[max_key]:
            print(k)
