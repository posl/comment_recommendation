def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)
main()
I'm trying to make a program that will take a string of numbers and separate them into a list of lists. For example, if the string is "123456789" the output should be [[1,2,3],[4,5,6],[7,8,9]]. I know how to do this with a list comprehension but I'm having trouble doing it with a generator.
I've been trying to create a program that will take a string of numbers and separate them into a list of lists. For example, if the string is "123456789" the output should be [[1,2,3],[4,5,6],[7,8,9]]. I know how to do this with a list comprehension but I'm having trouble doing it with a generator.
I have a string like this: '2016-06-23 17:00:00' and I want to convert it into a datetime object. I have tried a few things, but I am not getting the result I want. I am not sure how to use the strptime() function.
I'm trying to create a program that will take a string of numbers and separate them into a list of lists. For example, if the string is "123456789" the output should be [[1,2,3],[4,5,6],[7,8,9]]. I know how to do this with a list comprehension but I'm having trouble doing it with a generator.
I have a string like this: '2016-06-23 17:00:00' and I want to convert it into a datetime object. I have tried a few things, but I am not getting the result I want. I am not sure how to use the strptime() function.
I have a string like this: '2016-06-23 17:00:00' and I want to convert it into a datetime object. I have tried a few things, but I am not getting the

if __name__ == '__main__':
    main()