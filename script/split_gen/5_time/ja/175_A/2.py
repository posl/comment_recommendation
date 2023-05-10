def main():
    s = input()
    l = 0
    r = 0
    for i in s:
        if i == 'R':
            r += 1
            l = 0
        else:
            l += 1
            r = 0
    print(max(r, l))
