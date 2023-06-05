def get_max_happy_person_number(n, p):
    happy_person_number = 0
    for i in range(0, n):
        if i == 0:
            if p[n-1] == i or p[i] == i or p[i+1] == i:
                happy_person_number += 1
        elif i == n-1:
            if p[i-1] == i or p[i] == i or p[0] == i:
                happy_person_number += 1
        else:
            if p[i-1] == i or p[i] == i or p[i+1] == i:
                happy_person_number += 1
    return happy_person_number

if __name__ == '__main__':
    get_max_happy_person_number()