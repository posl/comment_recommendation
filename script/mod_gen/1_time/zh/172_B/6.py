def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()