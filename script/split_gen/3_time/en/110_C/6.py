def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)) == 26:
        print('Yes')
    else:
        print('No')
main()
