def bingo():
    a = []
    for i in range(3):
        a.append(input().split())
    n = input()
    b = []
    for i in range(n):
        b.append(input())
    for i in range(3):
        if a[i][0] in b and a[i][1] in b and a[i][2] in b:
            return "Yes"
        if a[0][i] in b and a[1][i] in b and a[2][i] in b:
            return "Yes"
    if a[0][0] in b and a[1][1] in b and a[2][2] in b:
        return "Yes"
    if a[0][2] in b and a[1][1] in b and a[2][0] in b:
        return "Yes"
    return "No"
print(bingo())

if __name__ == '__main__':
    bingo()