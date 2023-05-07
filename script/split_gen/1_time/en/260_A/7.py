def main():
    S = input()
    S = S.lower()
    for i in S:
        if S.count(i) == 1:
            print(i)
            break
    else:
        print(-1)
