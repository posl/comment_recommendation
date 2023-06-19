def main():
    num = int(input())
    odd = 0
    for i in range(1, num+1):
        if i % 2 == 1:
            odd += 1
    print(odd/num)

if __name__ == '__main__':
    main()