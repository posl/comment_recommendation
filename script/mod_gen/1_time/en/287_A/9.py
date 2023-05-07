def count_for(list):
    counter = 0
    for item in list:
        if item == 'For':
            counter += 1
    return counter
number_of_people = int(input())
people = []
for i in range(number_of_people):
    people.append(input())

if __name__ == '__main__':
    count_for()