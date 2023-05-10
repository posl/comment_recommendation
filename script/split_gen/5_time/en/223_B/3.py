def main():
    S = input()
    min_str = S
    max_str = S
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if min_str > S:
            min_str = S
        if max_str < S:
            max_str = S
    print(min_str)
    print(max_str)
main()
