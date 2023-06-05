def get_second_player(n, scores):
    if n == 1:
        return scores[0] if scores[0] > scores[1] else scores[1]
    else:
        first_half = get_second_player(n - 1, scores[:2 ** (n - 1)])
        second_half = get_second_player(n - 1, scores[2 ** (n - 1):])
        return first_half if first_half > second_half else second_half

if __name__ == '__main__':
    get_second_player()