def main():
    K = int(input())
    #print(K)
    H = K // 60
    #print(H)
    M = K % 60
    #print(M)
    if H < 10:
        H = "0" + str(H)
    if M < 10:
        M = "0" + str(M)
    print(str(21 + int(H)) + ":" + str(M))

if __name__ == '__main__':
    main()