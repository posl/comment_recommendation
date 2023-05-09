def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i % 10 == 0:
            continue
        else:
            for j in range(1,n+1):
                if j % 10 == 0:
                    continue
                else:
                    if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()