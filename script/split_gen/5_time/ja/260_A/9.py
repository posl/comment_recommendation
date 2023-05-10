def main():
    S = input()
    for i in S:
        if S.count(i) == 1:
            print(i)
            return
    print(-1)
main()
