def check_nickname(name, people):
    if name in people:
        return False
    else:
        return True
n = int(input())
people = []
for i in range(n):
    s, t = input().split()
    people.append(s)
    people.append(t)
for i in range(len(people)):
    if check_nickname(people[i], people[:i] + people[i+1:]):
        print("Yes")
        break
else:
    print("No")
