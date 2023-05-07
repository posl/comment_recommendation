def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_dict = {}
    for s in S:
        if s in S_dict:
            S_dict[s] += 1
        else:
            S_dict[s] = 1
    max_count = max(S_dict.values())
    for k, v in sorted(S_dict.items()):
        if v == max_count:
            print(k)
