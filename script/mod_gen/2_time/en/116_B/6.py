def main():
    s = int(input())
    a = [s]
    for i in range(1,1000000):
        if a[i-1]%2 == 0:
            a.append(a[i-1]//2)
        else:
            a.append(3*a[i-1]+1)
        if a[i] in a[:i]:
            print(i+1)
            break

if __name__ == '__main__':
    main()