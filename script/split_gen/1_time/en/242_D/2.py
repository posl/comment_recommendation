def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            print(S[k-1])
        else:
            if k % 3 == 1:
                print(S[0])
            elif k % 3 == 2:
                print(S[1])
            else:
                print(S[2])
