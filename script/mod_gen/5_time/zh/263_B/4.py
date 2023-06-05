def get_generation_count(persons, person_id):
    if person_id == 1:
        return 0
    else:
        return get_generation_count(persons, persons[person_id - 1]) + 1

if __name__ == '__main__':
    get_generation_count()