def main():
    S = input()
    T = input()
    count = 1000
    for i in range(len(S)-len(T)+1):
        count_tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count_tmp += 1
        if count_tmp < count:
            count = count_tmp
    print(count)

if __name__ == '__main__':
    main()