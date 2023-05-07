def main():
    S = input()
    S = sorted(S)
    S = S[::-1]
    #print(S)
    for i in range(0, len(S)):
        for j in range(i+1, len(S)):
            for k in range(j+1, len(S)):
                s = int(S[i] + S[j] + S[k])
                if s % 8 == 0:
                    print('Yes')
                    return
    print('No')
