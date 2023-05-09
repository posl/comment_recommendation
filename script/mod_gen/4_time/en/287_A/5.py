def main():
    no_of_people = int(input())
    people = []
    for i in range(no_of_people):
        people.append(input())
    if people.count('For') > people.count('Against'):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()