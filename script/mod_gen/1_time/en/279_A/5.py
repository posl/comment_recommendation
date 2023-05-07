def main():
    s = input()
    print(s.count('v') * (s.count('v') - 1) // 2)

if __name__ == '__main__':
    main()