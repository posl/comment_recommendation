def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append("")
    max = 0
    max_name = ""
    current_count = 0
    current_name = ""
    for i in range(N + 1):
        if current_name != S[i]:
            if current_count > max:
                max = current_count
                max_name = current_name
            current_name = S[i]
            current_count = 1
        else:
            current_count += 1
    print(max_name)
main()

if __name__ == '__main__':
    main()