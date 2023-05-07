def main():
    S = input()
    for i in range(0, len(S)):
        for j in range(i, len(S)):
            for k in range(j, len(S)):
                if int(S[i] + S[j] + S[k]) % 8 == 0:
                    print('Yes')
                    return
    print('No')
