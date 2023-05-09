def main():
    #input
    k = int(input())
    #compute
    hour = k//60
    minute = k%60
    #output
    print("{0:02d}:{1:02d}".format(hour+21,minute))

if __name__ == '__main__':
    main()