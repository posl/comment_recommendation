def round_down(x):
    if x.find('.') == -1:
        return x
    else:
        return x[:x.find('.')]

if __name__ == '__main__':
    round_down()