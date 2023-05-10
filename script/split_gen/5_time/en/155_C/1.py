def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S_dict = {}
    for s in S:
        if s in S_dict:
            S_dict[s] += 1
        else:
            S_dict[s] = 1
    max_S = max(S_dict.values())
    for s in S:
        if S_dict[s] == max_S:
            print(s)
            S_dict[s] = 0
