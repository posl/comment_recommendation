def main():
    #data = input().split()
    #c1 = data[0]
    #c2 = data[1]
    #c3 = data[2]
    #if c1 == c2 and c2 == c3:
    #    print("Won")
    #else:
    #    print("Lost")
    print("Won" if len(set(input())) == 1 else "Lost")

if __name__ == '__main__':
    main()