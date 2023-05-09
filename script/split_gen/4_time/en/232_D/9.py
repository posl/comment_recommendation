def main():
    i = input().split()
    h = int(i[0])
    w = int(i[1])
    a = []
    for j in range(h):
        a.append(input())
    ans = 1
    i = 0
    j = 0
    while True:
        if i == h-1 and j == w-1:
            break
        if i == h-1:
            if a[i][j+1] == ".":
                ans += 1
                j += 1
            else:
                break
        elif j == w-1:
            if a[i+1][j] == ".":
                ans += 1
                i += 1
            else:
                break
        else:
            if a[i][j+1] == "." and a[i+1][j] == ".":
                ans += 1
                if a[i][j+1] == "." and a[i+1][j] == ".":
                    if a[i+1][j+1] == ".":
                        if a[i][j+1] == ".":
                            j += 1
                        else:
                            i += 1
                    else:
                        if a[i][j+1] == ".":
                            j += 1
                        else:
                            i += 1
                else:
                    if a[i][j+1] == ".":
                        j += 1
                    else:
                        i += 1
            else:
                break
    print(ans)
