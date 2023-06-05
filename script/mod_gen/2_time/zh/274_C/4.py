def main():
    h, w = map(int, input().split())
    #print(h, w)
    data = [0 for i in range(w)]
    #print(data)
    for i in range(h):
        row = input()
        #print(row)
        for j in range(w):
            #print(row[j])
            if row[j] == '#':
                data[j] += 1
    #print(data)
    for i in range(w):
        print(data[i], end=' ')
    print()

if __name__ == '__main__':
    main()