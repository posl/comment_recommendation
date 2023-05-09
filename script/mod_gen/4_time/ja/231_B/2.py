def main():
    N = int(input())
    S = [input() for i in range(N)]
    S_set = set(S)
    S_dict = {}
    for s in S_set:
        S_dict[s] = 0
    for s in S:
        S_dict[s] += 1
    print(max(S_dict, key=S_dict.get))

if __name__ == '__main__':
    main()