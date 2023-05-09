def main():
    #read input
    X = int(input())
    
    #calculate output
    if X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    else:
        print('expert')

if __name__ == '__main__':
    main()