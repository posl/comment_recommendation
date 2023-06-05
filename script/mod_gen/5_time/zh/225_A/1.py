def main():
    s = input()
    #print(s)
    #print(len(s))
    set_s = set(s)
    #print(set_s)
    #print(len(set_s))
    #print(len(s)-len(set_s))
    if len(s)-len(set_s) == 0:
        print(6)
    elif len(s)-len(set_s) == 1:
        print(3)
    else:
        print(1)
    return 0

if __name__ == '__main__':
    main()