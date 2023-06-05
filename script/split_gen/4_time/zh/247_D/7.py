def main():
    n = int(input())
    s = []
    for i in range(n):
        a = list(map(int, input().split()))
        if a[0] == 1:
            for j in range(a[2]):
                s.append(a[1])
        else:
            print(sum(s[:a[1]]))
            s = s[a[1]:]
