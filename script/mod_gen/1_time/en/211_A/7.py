def mean_arterial_pressure(systolic, diastolic):
    return (systolic - diastolic) / 3 + diastolic

if __name__ == '__main__':
    mean_arterial_pressure()