def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        a = 0
        b = r-1
        while a < b:
            if c[a] == 'W':
                while c[b] == 'W':
                    b -= 1
                c = c[:a] + 'R' + c[a+1:b] + 'W' + c[b+1:]
            a += 1
        print(c.count('W'))
    return 0
