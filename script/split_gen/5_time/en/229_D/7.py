def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ').split()
    S = [len(s) for s in S]
    S = [max(s - 2 * K, 0) for s in S]
    print(max(S))
