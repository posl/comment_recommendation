def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    count = 0
    for i in range(S_len-T_len+1):
        for j in range(T_len):
            if S[i+j] != T[j]:
                count += 1
    print(count)
