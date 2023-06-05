def get_answer(h):
    if h == 1:
        return 1
    else:
        return 2*get_answer(h//2) + 1

if __name__ == '__main__':
    get_answer()