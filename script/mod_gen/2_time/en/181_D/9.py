def main():
    S = input()
    
    if S.count("8") > 0:
        print("Yes")
        exit()
    
    for i in range(1, len(S)):
        for j in range(0, len(S)-i):
            if (int(S[j:j+i+1]) % 8) == 0:
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()