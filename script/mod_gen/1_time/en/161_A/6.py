def main():
    #Get Input
    x,y,z = map(int, input().split())
    #Swap the contents of the boxes A and B
    x,y = y,x
    #Swap the contents of the boxes A and C
    x,z = z,x
    #Print Output
    print(x,y,z)

if __name__ == '__main__':
    main()