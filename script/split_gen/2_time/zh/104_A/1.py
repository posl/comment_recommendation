def get_next_game_name(score):
    if score < 1200:
        return "ABC"
    elif score < 2800:
        return "ARC"
    else:
        return "AGC"
