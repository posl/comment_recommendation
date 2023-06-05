def main():
    n, x = input().split()
    n = int(n)
    x = int(x)
    s = input()
    #print(n, x, s)
    result = x
    for i in range(n):
        if s[i] == 'U':
            result = result // 2
        elif s[i] == 'L':
            result = result * 2 - 1
        elif s[i] == 'R':
            result = result * 2 + 1
    print(result)
