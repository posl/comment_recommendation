def main():
    N = int(input())
    S = [input() for _ in range(N)]
    s_dict = {}
    for s in S:
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1
    for s in S:
        if s_dict[s] > 1:
            print(s + "(" + str(s_dict[s] - 1) + ")")
        else:
            print(s)
