def main():
    s = int(input())
    a = []
    a.append(s)
    i = 1
    while True:
        if a[i-1] % 2 == 0:
            a.append(a[i-1] // 2)
        else:
            a.append(3*a[i-1] + 1)
        if a[i] in a[:i]:
            break
        i += 1
    print(i+1)
