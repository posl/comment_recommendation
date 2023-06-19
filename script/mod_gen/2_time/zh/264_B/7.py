def main():
    R,C = map(int,input().split())
    for i in range(R):
        if i%2 == 0:
            for j in range(C):
                if j%2 == 0:
                    print('#',end='')
                else:
                    print('.',end='')
        else:
            for j in range(C):
                if j%2 == 0:
                    print('.',end='')
                else:
                    print('#',end='')
        print()

if __name__ == '__main__':
    main()