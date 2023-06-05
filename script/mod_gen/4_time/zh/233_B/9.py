def reverse_string(string, begin, end):
    """
    :param string: string to be reversed
    :param begin: begin index
    :param end: end index
    :return: reversed string
    """
    if begin >= end:
        return string
    else:
        string = string[:begin] + string[end] + string[begin + 1:end] + string[begin] + string[end + 1:]
        return reverse_string(string, begin + 1, end - 1)

if __name__ == '__main__':
    reverse_string()