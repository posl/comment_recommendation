def main():
    num_animal, num_leg = map(int, input().split())
    for num_turtle in range(num_animal + 1):
        num_crane = num_animal - num_turtle
        total_leg = 2 * num_crane + 4 * num_turtle
        if total_leg == num_leg:
            print("Yes")
            return
    print("No")
