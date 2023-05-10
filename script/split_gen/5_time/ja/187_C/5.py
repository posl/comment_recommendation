def main():
    N = int(input())
    S = [input() for i in range(N)]
    if len(S) == len(set(S)):
        print("satisfiable")
    else:
        print("".join(S))
