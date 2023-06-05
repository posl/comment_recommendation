def main():
    s = input()
    num_list = s.split()
    num_set = set(num_list)
    print(len(num_set))

if __name__ == '__main__':
    main()