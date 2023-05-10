def count_generation(amoebae, generation):
    if generation == 0:
        return 1
    else:
        return count_generation(amoebae, generation - 1) + count_generation(amoebae, generation - 1)
