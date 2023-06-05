def anima_legs_check(num_anima, num_legs):
    for num_tur in range(num_anima + 1):
        num_crane = num_anima - num_tur
        if 2 * num_crane + 4 * num_tur == num_legs:
            return True
    return False
