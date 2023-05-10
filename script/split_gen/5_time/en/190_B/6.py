def main():
    n, s, d = map(int, input().split())
    spells = [list(map(int, input().split())) for _ in range(n)]
    for x, y in spells:
        if x < s and y > d:
            print("Yes")
            return
    print("No")
