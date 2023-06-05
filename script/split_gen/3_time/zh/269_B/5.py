def main():
    s = []
    for i in range(10):
        s.append(input())
    print(s)
    for i in range(10):
        if '#' in s[i]:
            print(i)
            break
    for j in range(10):
        if '#' in s[i][j]:
            print(j)
            break
    for i in range(9, -1, -1):
        if '#' in s[i]:
            print(i)
            break
    for j in range(9, -1, -1):
        if '#' in s[i][j]:
            print(j)
            break
