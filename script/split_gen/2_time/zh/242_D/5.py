def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        if t == 0:
            print(s[k])
        elif t == 1:
            print(s[(k+1)%len(s)])
        else:
            print(s[(k+2)%len(s)])
