def main():
    s = input()
    l = len(s)
    count = 0
    for i in range(l):
        for j in range(i, l):
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
    print(count)
