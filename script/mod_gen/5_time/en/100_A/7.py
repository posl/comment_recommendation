def main():
    #print("Start")
    #print("Please input A and B with space")
    a,b = map(int, input().split())
    #print("A is " + str(a))
    #print("B is " + str(b))
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")

if __name__ == '__main__':
    main()