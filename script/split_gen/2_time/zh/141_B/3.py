def is_easy_to_play(str):
    is_even_pos = True
    for c in str:
        if is_even_pos:
            if c == 'L':
                return False
        else:
            if c == 'R':
                return False
        is_even_pos = not is_even_pos
    return True
