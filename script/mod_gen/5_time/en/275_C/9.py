def main():
    #get input
    input = []
    for i in range(9):
        input.append(list(input()))
    #initialize count
    count = 0
    #count
    for i in range(9):
        for j in range(9):
            if i + 1 < 9 and j + 1 < 9:
                if input[i][j] == '#' and input[i+1][j] == '#' and input[i][j+1] == '#' and input[i+1][j+1] == '#':
                    count += 1
    #print
    print(count)
main()

if __name__ == '__main__':
    main()