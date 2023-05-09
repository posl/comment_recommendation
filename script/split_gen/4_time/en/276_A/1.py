def main():
    input_str = input()
    if 'a' in input_str:
        print(input_str.rindex('a') + 1)
    else:
        print(-1)
main()
