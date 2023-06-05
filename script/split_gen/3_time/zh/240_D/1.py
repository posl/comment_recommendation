def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = []
    for i in range(n):
        while len(s) > 0 and s[-1] == a[i]:
            s.pop()
        s.append(a[i])
        print(len(s))
