def problem276_a():
    S = input()
    if 'a' in S:
        print(S.rfind('a') + 1)
    else:
        print(-1)

if __name__ == '__main__':
    problem276_a()