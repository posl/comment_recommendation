def get_answer(h):
    if h == 1:
        return 1
    else:
        return 2*get_answer(h//2) + 1
