def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if len(set(S) & set(T)) == M:
        print('Yes')
    else:
        print('No')
