def main():
    N = int(input())
    S = input()
    if N == 1:
        print(1)
        return
    slime = []
    for i in range(N):
        if i == 0:
            slime.append(S[i])
        elif slime[-1] != S[i]:
            slime.append(S[i])
    print(len(slime))
