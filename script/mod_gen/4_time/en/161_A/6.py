def main():
    #read in the values
    a,b,c = map(int,input().split())
    #swap the values
    a,b = b,a
    a,c = c,a
    #print the values
    print(a,b,c)

if __name__ == '__main__':
    main()