def main():
    S = input()
    if S == 'RRR':
        print(3)
    elif S == 'SRR' or S == 'RRS':
        print(2)
    elif S == 'SSS':
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()