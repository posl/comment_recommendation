def main():
    s = input()
    k = int(input())
    s = s.replace('.', ',')
    s = s.split(',')
    s = [len(i) for i in s]
    s = [i-k for i in s]
    s = [i for i in s if i>0]
    s = [i+k for i in s]
    print(max(s))

if __name__ == '__main__':
    main()