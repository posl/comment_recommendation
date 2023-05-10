def main():
    n,s,d = map(int, input().split())
    spells = [list(map(int, input().split())) for _ in range(n)]
    print("Yes" if any([spell[0] < s and spell[1] > d for spell in spells]) else "No")

if __name__ == '__main__':
    main()