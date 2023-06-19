def count_legs(num_animals, num_legs):
    for num_tur in range(num_animals + 1):
        num_crane = num_animals - num_tur
        if 2 * num_crane + 4 * num_tur == num_legs:
            return True
    return False
