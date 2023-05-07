def main():
    n = int(input())
    s = input()
    for i in range(n-1):
        l = 0
        for j in range(1, n-i):
            if s[i] != s[i+j]:
                l = j
        print(l)
