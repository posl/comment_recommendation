def main():
    S = input()
    T = input()
    min = 1000
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)
main()

if __name__ == '__main__':
    main()