def main():
    n, s, d = map(int, input().split())
    spells = []
    for i in range(n):
        spells.append(list(map(int, input().split())))
    for i in range(n):
        if spells[i][0] < s and spells[i][1] > d:
            print("Yes")
            break
        else:
            print("No")
            break
