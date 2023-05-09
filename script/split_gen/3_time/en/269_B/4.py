def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if "#" in s[i]:
            a = i
            break
    for i in range(9, -1, -1):
        if "#" in s[i]:
            b = i
            break
    for i in range(10):
        if "#" in [s[j][i] for j in range(10)]:
            c = i
            break
    for i in range(9, -1, -1):
        if "#" in [s[j][i] for j in range(10)]:
            d = i
            break
    print(a + 1, b + 1)
    print(c + 1, d + 1)
