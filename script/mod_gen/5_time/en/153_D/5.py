def main():
    H = int(input())
    print(2**(H.bit_length())-1)

if __name__ == '__main__':
    main()