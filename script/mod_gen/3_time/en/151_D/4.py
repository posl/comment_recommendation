def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    max = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                count = 0
                for k in range(h):
                    for l in range(w):
                        if s[k][l] == '.':
                            count += 1
                if count > max:
                    max = count
    print(max)

if __name__ == '__main__':
    main()