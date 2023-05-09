def missing_number():
    input_str = input()
    for i in range(1, 10):
        if str(i) not in input_str:
            print(i)
            break
