def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while l + i < n:
            if s[l] != s[l + i]:
                l += 1
            else:
                break
        print(l)
