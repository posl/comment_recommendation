def get_round_label(round_number):
    if round_number < 1000:
        return "ABC"
    else:
        return "ABD"

if __name__ == '__main__':
    get_round_label()