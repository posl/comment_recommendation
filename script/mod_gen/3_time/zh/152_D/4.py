def main():
    num = int(input())
    count = 0
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i%10 == j//10 and j%10 == i//10:
                count += 1
    print(count)

if __name__ == '__main__':
    main()