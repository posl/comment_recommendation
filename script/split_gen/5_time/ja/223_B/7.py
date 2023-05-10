def main():
    S = input()
    print(min(S[1:] + S[0], S[-1] + S[:-1]))
    print(max(S[1:] + S[0], S[-1] + S[:-1]))
main()
