def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
        else:
            break
    if K <= count:
        print(1)
        return
    else:
        print(S[count-1])
        return

if __name__ == '__main__':
    main()