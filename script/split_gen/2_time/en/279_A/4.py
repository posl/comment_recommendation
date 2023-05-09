def main():
    s = input()
    v = 0
    w = 0
    count = 0
    for i in s:
        if i == 'v':
            v += 1
        elif i == 'w':
            w += 1
        if v == w and v > 0:
            count += 1
    print(count)
