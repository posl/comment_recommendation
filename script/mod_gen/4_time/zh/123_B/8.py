def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    time = 0
    time += (A-1)//10*10 + A
    time += (B-1)//10*10 + B
    time += (C-1)//10*10 + C
    time += (D-1)//10*10 + D
    time += (E-1)//10*10 + E
    print(time)

if __name__ == '__main__':
    main()