def main():
    N = int(input())
    s = [input().split() for _ in range(N)]
    for i in range(N):
        if s[i][0] in s[i][1] or s[i][1] in s[i][0]:
            continue
        else:
            print("No")
            break
    else:
        print("Yes")
