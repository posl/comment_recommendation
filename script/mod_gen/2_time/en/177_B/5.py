def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    minChanges = lenT
    for i in range(lenS - lenT + 1):
        changes = 0
        for j in range(lenT):
            if S[i + j] != T[j]:
                changes += 1
        if changes < minChanges:
            minChanges = changes
    print(minChanges)

if __name__ == '__main__':
    main()