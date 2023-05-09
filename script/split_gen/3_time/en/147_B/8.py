def main():
    S = input()
    S1 = S[:len(S)//2]
    S2 = S[len(S)//2+len(S)%2:]
    S2 = S2[::-1]
    count = 0
    for i in range(len(S1)):
        if S1[i] != S2[i]:
            count += 1
    print(count)
