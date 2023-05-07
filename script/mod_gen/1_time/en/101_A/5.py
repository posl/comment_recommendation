def main():
    # get input
    s = input()
    # count + and - and print sum
    print(s.count('+') - s.count('-'))

if __name__ == '__main__':
    main()