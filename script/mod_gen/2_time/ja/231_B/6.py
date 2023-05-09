def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max = 0
    max_name = ""
    name = ""
    for i in range(N):
        if name == S[i]:
            max += 1
        else:
            name = S[i]
            max = 1
        if max > max_name:
            max_name = name
    print(max_name)

if __name__ == '__main__':
    main()