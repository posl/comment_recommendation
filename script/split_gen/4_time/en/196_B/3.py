def round_down(x):
    if x.find('.') == -1:
        return x
    else:
        return x[:x.find('.')]
