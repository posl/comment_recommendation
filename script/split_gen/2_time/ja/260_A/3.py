def main():
    S = input()
    ans = -1
    for i in S:
        if S.count(i) == 1:
            ans = i
            break
    print(ans)
