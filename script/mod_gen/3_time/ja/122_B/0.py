def main():
    S = input()
    S = S.replace('A','1')
    S = S.replace('C','1')
    S = S.replace('G','1')
    S = S.replace('T','1')
    S = S.replace('0','0')
    #print(S)
    S = S.split('0')
    #print(S)
    print(len(max(S)))

if __name__ == '__main__':
    main()