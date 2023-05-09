def main():
    n = int(input())
    people = []
    for i in range(n):
        people.append(input())
    if len(people) == len(set(people)):
        print("No")
    else:
        print("Yes")
