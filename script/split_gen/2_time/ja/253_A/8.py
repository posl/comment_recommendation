def main():
    abclist = list(map(int, input().split()))
    abclist.sort()
    if abclist[1] == abclist[0] or abclist[1] == abclist[2]:
        print("Yes")
    else:
        print("No")
