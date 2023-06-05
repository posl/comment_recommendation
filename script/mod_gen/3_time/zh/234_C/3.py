def main():
    k = int(input())
    l = []
    l.append(2)
    l.append(20)
    l.append(22)
    for i in range(3,k+1):
        l.append(int(str(l[i-1])+'2'))
        l.append(int(str(l[i-2])+'0'))
        l.append(int(str(l[i-3])+'2'))
    print(l[k-1])

if __name__ == '__main__':
    main()