def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        s = list(map(int, input().split()))
        if s[0] == 1:
            a[s[1] - 1] = s[2]
        else:
            print(a[s[1] - 1])
