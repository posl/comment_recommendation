def main():
    while True:
        try:
            line = input()
            if line == '':
                break
            line = line.split(' ')
            N = int(line[0])
            A = int(line[1])
            B = int(line[2])
            for i in range(N):
                for j in range(A):
                    for k in range(N):
                        for l in range(B):
                            if (i+j)%2 == 0:
                                print('.',end='')
                            else:
                                print('#',end='')
                    print()
        except:
            break

if __name__ == '__main__':
    main()