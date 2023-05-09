def main():
    #input
    K = int(input())
    #output
    print(str((21+K//60)%24)+":"+str(K%60).zfill(2))

if __name__ == '__main__':
    main()