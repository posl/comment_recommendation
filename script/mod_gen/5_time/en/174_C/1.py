def main():
    k = int(input())
    seven = 7
    for i in range(k):
        if seven % k == 0:
            print(i+1)
            break
        else:
            seven = seven * 10 + 7
    else:
        print(-1)

if __name__ == '__main__':
    main()