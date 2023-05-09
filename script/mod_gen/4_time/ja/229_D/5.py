def main():
    s = input()
    k = int(input())
    if k == 0:
        print(max([len(i) for i in s.split('.')]))
    else:
        s = s.replace('X', '1').replace('.', '0')
        print(max([len(i) for i in s.split('0')]) + k)

if __name__ == '__main__':
    main()