def main():
    #Read the input
    M, H = map(int, input().split(" "))
    #If the monster's health is a multiple of M, then Takahashi's magic can defeat it
    if H % M == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()