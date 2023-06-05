def is_drawable(lengths):
    max_length = max(lengths)
    if sum(lengths) - max_length > max_length:
        return '是'
    else:
        return '否'
