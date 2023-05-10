def main():
    n = int(input())
    s = input()
    #print(n)
    #print(s)
    l = list(s)
    #print(l)
    for i in range(len(l)):
        l[i] = ord(l[i]) + n
        #print(l[i])
        if l[i] > ord('Z'):
            l[i] = l[i] - ord('Z') + ord('A') - 1
        l[i] = chr(l[i])
        #print(l[i])
    print(''.join(l))

if __name__ == '__main__':
    main()