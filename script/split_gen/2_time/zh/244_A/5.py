def main():
    n,x = map(int,input().split())
    s = input()
    x = x - 1
    for i in range(n):
        if s[i] == 'U':
            x = x // 2
        elif s[i] == 'L':
            x = 2*x + 1
        else:
            x = 2*x + 2
    print(x+1)
