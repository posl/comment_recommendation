def main():
    s = int(input())
    a = [s]
    i = 1
    while True:
        i += 1
        if a[-1] % 2 == 0:
            a.append(a[-1] / 2)
        else:
            a.append(3 * a[-1] + 1)
        if a.count(a[-1]) == 2:
            print(i)
            break
