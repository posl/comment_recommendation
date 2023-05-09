def main():
    n,s,d = map(int, input().split())
    spells = [list(map(int, input().split())) for _ in range(n)]
    for spell in spells:
        if spell[0] < s and spell[1] > d:
            print('Yes')
            return
    print('No')
