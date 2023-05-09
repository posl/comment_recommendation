def distinct_integers():
    input_string = input()
    input_list = input_string.split()
    input_set = set(input_list)
    print(len(input_set))
distinct_integers()

if __name__ == '__main__':
    distinct_integers()