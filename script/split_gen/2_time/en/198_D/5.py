def main():
    S = [input() for _ in range(3)]
    N = [len(s) for s in S]
    if max(N) > 10:
        print('UNSOLVABLE')
        return
    if max(N) == 10:
        if len(set(S[0])) == 1 and len(set(S[1])) == 1 and len(set(S[2])) == 1:
            if S[0][0] == S[1][0] and S[1][0] == S[2][0]:
                print('UNSOLVABLE')
                return
    if N[0] > N[1]:
        S[0], S[1] = S[1], S[0]
        N[0], N[1] = N[1], N[0]
    if N[1] > N[2]:
        S[1], S[2] = S[2], S[1]
        N[1], N[2] = N[2], N[1]
    if N[0] > N[1]:
        S[0], S[1] = S[1], S[0]
        N[0], N[1] = N[1], N[0]
    if N[0] == N[1] == N[2] == 1:
        if S[0] == S[1] and S[1] == S[2]:
            print('UNSOLVABLE')
            return
        else:
            print(1)
            print(1)
            print(2)
            return
    if N[0] == N[1] == N[2] == 2:
        if S[0] == S[1] and S[1] == S[2]:
            print('UNSOLVABLE')
            return
        else:
            print(10)
            print(10)
            print(20)
            return
    if N[0] == N[1] == 1:
        if S[0] == S[1]:
            print('UNSOLVABLE')
            return
        else:
            print(1)
            print(1)
            print(2)
            return
    if N[1] == N[2] == 1:
        if S[1] == S[2]:
