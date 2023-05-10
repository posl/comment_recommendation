def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if m > n:
        print("No")
        return
    for i in range(n):
        if s[i] == t[0]:
            break
    else:
        print("No")
        return
    for j in range(m):
        if s[j+i] != t[j]:
            print("No")
            return
    print("Yes")
