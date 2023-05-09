def main():
    s = input()
    c = 0
    max = 0
    for i in range(3):
        if s[i] == 'R':
            c += 1
        else:
            c = 0
        if max < c:
            max = c
    print(max)
