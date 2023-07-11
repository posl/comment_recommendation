def main():
    n = int(input())
    list1 = []
    for i in range(n):
        list1.append(int(input()))
    for i in range(n):
        print(list1[i]//2)

if __name__ == '__main__':
    main()