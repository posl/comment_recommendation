def main():
    strings = []
    for i in range(10):
        strings.append(input())
    #print(strings)
    for i in range(10):
        for j in range(10):
            if strings[i][j] == '#':
                print(i+1,j+1)
                exit()
