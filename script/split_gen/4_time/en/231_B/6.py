def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(set(S), key=S.count))
main()
