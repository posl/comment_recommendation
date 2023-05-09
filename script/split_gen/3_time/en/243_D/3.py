def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'L':
            x = 2*x
        elif s[i] == 'R':
            x = 2*x + 1
        else:
            x = (x+1)//2
    print(x)
