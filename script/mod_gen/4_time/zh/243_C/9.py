def get_input():
    N = int(input())
    people = []
    for i in range(N):
        people.append(list(map(int, input().split())))
    S = input()
    return people, S

if __name__ == '__main__':
    get_input()