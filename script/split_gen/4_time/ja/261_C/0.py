def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {}
    for s in S:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
        print(s if dic[s] == 1 else s + '(' + str(dic[s] - 1) + ')')
