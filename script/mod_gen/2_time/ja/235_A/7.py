def main():
    abc = input()
    print(int(abc) + int(abc[1:]+abc[0]) + int(abc[2]+abc[:2]))

if __name__ == '__main__':
    main()