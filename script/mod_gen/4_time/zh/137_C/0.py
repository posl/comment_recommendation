def make_dict(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

if __name__ == '__main__':
    make_dict()