def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')
