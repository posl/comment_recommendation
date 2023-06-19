def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    print(S[-1])
