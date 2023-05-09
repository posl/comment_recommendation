def main():
    p_list = list(map(int, input().split()))
    a_list = [chr(96 + p) for p in p_list]
    print(''.join(a_list))

if __name__ == '__main__':
    main()