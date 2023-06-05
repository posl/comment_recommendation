def main():
    s = input()
    l = len(s)
    count = 0
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            count += 1
    print(count)
