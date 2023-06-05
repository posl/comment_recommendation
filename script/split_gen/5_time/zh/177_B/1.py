def main():
    S = input()
    T = input()
    sLen = len(S)
    tLen = len(T)
    min = 1000
    for i in range(sLen - tLen + 1):
        count = 0
        for j in range(tLen):
            if S[i + j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)
