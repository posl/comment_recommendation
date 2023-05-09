def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dict = {}
    for s in S:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    print(max(dict, key=dict.get))
