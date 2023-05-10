def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
        return
    for i in range(3):
        if int(x[i+1]) != (int(x[i])+1)%10:
            print("Strong")
            return
    print("Weak")

if __name__ == '__main__':
    main()