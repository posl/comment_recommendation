def main():
    S = input()
    max_len = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            if S[i:j].isalpha():
                if S[i:j].count('A') + S[i:j].count('C') + S[i:j].count('G') + S[i:j].count('T') == len(S[i:j]):
                    max_len = max(max_len,len(S[i:j]))
    print(max_len)

if __name__ == '__main__':
    main()