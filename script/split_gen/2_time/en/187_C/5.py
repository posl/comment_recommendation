def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_set = set(S)
    for s in S:
        if '!' + s in S_set:
            print(s)
            return
    print('satisfiable')
