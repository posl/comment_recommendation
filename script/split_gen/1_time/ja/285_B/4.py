def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for j in range(n-i):
            if s[j] != s[j+i]:
                l += 1
            else:
                break
        print(l)
