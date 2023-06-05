def main():
    s = []
    for i in range(10):
        s.append(list(input()))
    #print(s)
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if i == 0:
                    a = i
                else:
                    a = i - 1
                if j == 0:
                    b = j
                else:
                    b = j - 1
                if i == 9:
                    c = i
                else:
                    c = i + 1
                if j == 9:
                    d = j
                else:
                    d = j + 1
                for k in range(a,c+1):
                    for l in range(b,d+1):
                        s[k][l] = "#"
    for i in range(10):
        print("".join(s[i]))

if __name__ == '__main__':
    main()