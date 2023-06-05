def main():
    k = int(input())
    sum = 0
    for i in range(1,k+1):
        if i % 2 == 0:
            for j in range(1,k+1):
                if j % 2 == 1:
                    sum += 1
        else:
            for j in range(1,k+1):
                if j % 2 == 0:
                    sum += 1
    print(sum)

if __name__ == '__main__':
    main()