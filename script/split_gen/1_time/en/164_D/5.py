def main():
    s = input()
    l = len(s)
    c = 0
    for i in range(l):
        for j in range(i+1, l+1):
            if int(s[i:j]) % 2019 == 0:
                c += 1
    print(c)
