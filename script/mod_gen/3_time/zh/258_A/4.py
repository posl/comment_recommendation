def main():
    K = int(input())
    H = K//60
    M = K%60
    print(str(21+H).zfill(2)+":"+str(M).zfill(2))

if __name__ == '__main__':
    main()