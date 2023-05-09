def main():
    N = int(input())
    S = [input() for _ in range(N)]
    count = {}
    for s in S:
        if s not in count:
            count[s] = 1
            print(s)
        else:
            print(s + '(' + str(count[s]) + ')')
            count[s] += 1
