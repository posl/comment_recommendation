def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(max(set(S), key=S.count))

if __name__ == '__main__':
    main()