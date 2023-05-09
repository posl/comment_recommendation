def main():
    a, b = map(int, input().split())
    if (b - a) in [1, 9]:
        print("Yes")
    else:
        print("No")
    
main()

if __name__ == '__main__':
    main()