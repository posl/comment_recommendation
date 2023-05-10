def main():
    input = input()
    print(input.count('0')*2 if input.count('0')*2 < len(input) else len(input))
main()

if __name__ == '__main__':
    main()