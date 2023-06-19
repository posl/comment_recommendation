def get_max_name(names):
    max_name = ""
    max_count = 0
    for name in names:
        if names.count(name) > max_count:
            max_count = names.count(name)
            max_name = name
    return max_name

if __name__ == '__main__':
    get_max_name()