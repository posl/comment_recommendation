def get_name():
    name_list = []
    while True:
        try:
            name = input()
            if name == "":
                break
            name_list.append(name)
        except EOFError:
            break
    return name_list

if __name__ == '__main__':
    get_name()