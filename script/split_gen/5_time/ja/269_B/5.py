def main():
    s = [input() for _ in range(10)]
    #print(s)
    for i in range(10):
        if s[i].count('#') >= 2:
            a = i
            break
    for i in range(9, -1, -1):
        if s[i].count('#') >= 2:
            b = i
            break
    for i in range(10):
        if '#' in [s[j][i] for j in range(10)]:
            c = i
            break
    for i in range(9, -1, -1):
        if '#' in [s[j][i] for j in range(10)]:
            d = i
            break
    print(a+1, b+1)
    print(c+1, d+1)
