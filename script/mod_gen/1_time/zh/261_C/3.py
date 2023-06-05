def print_new_name(n, names):
    name_dict = {}
    for name in names:
        if name in name_dict:
            name_dict[name] += 1
            print(name + '(' + str(name_dict[name]) + ')')
        else:
            name_dict[name] = 0
            print(name)

if __name__ == '__main__':
    print_new_name()