def main():
    N = int(input())
    S = input()
    if N == 1:
        print(1)
        return
    slime = []
    for i in range(N):
        slime.append(S[i])
    i = 0
    while i < len(slime)-1:
        if slime[i] == slime[i+1]:
            del slime[i+1]
        else:
            i += 1
    print(len(slime))
main()
