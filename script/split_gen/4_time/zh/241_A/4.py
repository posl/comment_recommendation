def get_next_number(number):
    return number_list[number]
number_list = list(map(int, input().split()))
number = 0
for _ in range(3):
    number = get_next_number(number)
print(number)
