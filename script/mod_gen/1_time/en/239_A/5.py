def main():
    H = int(input())
    print(((12800000+H)*H)**(1/2))
main()
I made this program for a contest. I think it's correct, but the judge says it's wrong. I don't know why. Can someone explain to me what's wrong with it?
I think it's because of the floating point error. I tried to change the code like this:

if __name__ == '__main__':
    main()