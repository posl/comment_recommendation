def getPerson(N, K, A):
    person = (A + K - 1) % N
    if person == 0:
        person = N
    return person

if __name__ == '__main__':
    getPerson()