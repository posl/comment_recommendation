def main():
    age, cost = map(int, input().split())
    if age < 6:
        print(0)
    elif age < 13:
        print(cost // 2)
    else:
        print(cost)
main()
I think it's a good idea to use the input() function with the map() function to convert the input into the desired type.
