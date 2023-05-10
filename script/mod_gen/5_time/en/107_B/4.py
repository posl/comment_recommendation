def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(h):
        if a[i].count(".") == w:
            a[i] = ""
    for i in range(w):
        count = 0
        for j in range(h):
            if a[j] != "":
                if a[j][i] == ".":
                    count += 1
        if count == h:
            for j in range(h):
                a[j] = a[j][:i] + a[j][i+1:]
    for i in range(h):
        if a[i] != "":
            print(a[i])

if __name__ == '__main__':
    main()