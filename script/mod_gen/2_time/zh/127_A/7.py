def ride_ferris_wheel(age, fee):
    if age >= 13:
        return fee
    elif age >= 6 and age <= 12:
        return fee / 2
    else:
        return 0

if __name__ == '__main__':
    ride_ferris_wheel()