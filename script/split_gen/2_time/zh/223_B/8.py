def main():
    s = input()
    n = len(s)
    s = s+s
    min_s = s[:n]
    max_s = s[:n]
    for i in range(1,n):
        if s[i:i+n] < min_s:
            min_s = s[i:i+n]
        if s[i:i+n] > max_s:
            max_s = s[i:i+n]
    print(min_s)
    print(max_s)
