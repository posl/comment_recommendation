def main():
    N = int(input())
    S = [input() for i in range(N)]
    S = list(set(S))
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')
    return

if __name__ == '__main__':
    main()