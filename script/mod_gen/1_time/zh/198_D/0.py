def getint(str):
    x = 0
    for i in range(len(str)):
        x += (ord(str[i]) - ord('a') + 1) * (10 ** (len(str) - i - 1))
    return x
S1 = input()
S2 = input()
S3 = input()
S1_int = getint(S1)
S2_int = getint(S2)
S3_int = getint(S3)
for i in range(10 ** (len(S1) - 1), 10 ** len(S1)):
    for j in range(10 ** (len(S2) - 1), 10 ** len(S2)):
        for k in range(10 ** (len(S3) - 1), 10 ** len(S3)):
            if i + j == k:
                if getint(S1) == i and getint(S2) == j and getint(S3) == k:
                    print(i)
                    print(j)
                    print(k)
                    exit()
print("UNSOLVABLE")

if __name__ == '__main__':
    getint()