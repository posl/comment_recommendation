def main():
    # 1. input
    s = input()
    # 2. process
    # 2.1. create a list of possible triplets
    # 2.2. calculate the absolute difference between each triplet and 753
    # 2.3. return the minimum of the differences
    # 3. output
    print(min([abs(int(s[i:i+3]) - 753) for i in range(len(s)-2)]))

if __name__ == '__main__':
    main()