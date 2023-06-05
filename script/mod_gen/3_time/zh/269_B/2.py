def main():
    strs = []
    for i in range(10):
        strs.append(input())
    for i in range(10):
        for j in range(10):
            if strs[i][j] == '#':
                print(i+1,j+1)
                break
main()
