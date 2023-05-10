def ferris_wheel():
    age, cost = map(int, input().split())
    if age <= 5:
        print(0)
    elif age in range(6, 13):
        print(cost//2)
    else:
        print(cost)

if __name__ == '__main__':
    ferris_wheel()