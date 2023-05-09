def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    i = 0
    j = 0
    while i < n:
        if s[i] == t[j]:
            j += 1
            if j == m:
                break
        i += 1
    if j == m:
        print("Yes")
    else:
        print("No")
