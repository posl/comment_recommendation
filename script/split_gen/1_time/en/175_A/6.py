def main():
    S = input()
    maxRainyDays = 0
    currentRainyDays = 0
    for i in range(3):
        if S[i] == 'R':
            currentRainyDays += 1
            if currentRainyDays > maxRainyDays:
                maxRainyDays = currentRainyDays
        else:
            currentRainyDays = 0
    print(maxRainyDays)
