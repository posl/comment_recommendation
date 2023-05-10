def getMeanArterialPressure(systolicBloodPressure, diastolicBloodPressure):
    return (systolicBloodPressure - diastolicBloodPressure) / 3 + diastolicBloodPressure

if __name__ == '__main__':
    getMeanArterialPressure()