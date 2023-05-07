def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    a = [0] * 3
    b = [0] * 3
    for i in range(3):
        a[i] = h[i] - w[i]
        b[i] = w[i] - h[i]
    ans = 0
    for i in range(1, 29):
        for j in range(1, 29):
            for k in range(1, 29):
                if i + j + k == a[0] and i + j + k == a[1] and i + j + k == a[2]:
                    if i * j * k == b[0] and i * j * k == b[1] and i * j * k == b[2]:
                        ans += 1
    print(ans)
main()
I have a list of 3 numbers, which I want to use as the first 3 numbers in a sequence of numbers. The next number in the sequence is the sum of the previous 3 numbers. I want to use this list of 3 numbers to generate a sequence of numbers with a length of 1000. I have tried to use a for loop, but I'm not sure how to do it. I'm also not sure how to generate the sequence of numbers. Any help would be appreciated.
I am trying to make a program that will take a list of numbers and then sort them into 2 lists. The first list will have all the even numbers and the second list will have all the odd numbers. I am trying to do this using a for loop and an if statement but I am not sure how to go about doing this. I have tried a couple of different ways but none of them have worked. Any help would be appreciated.
I am trying to make a program that will take a list of numbers and then sort them into 2 lists. The first list will have all the even numbers and the second list will have all the odd numbers. I am trying to do this using a for loop and an if statement but I am not sure how to go about doing this. I have tried a couple of different ways but none of them have worked. Any help would be appreciated.
I am trying to make a program that will take a list of numbers and then sort them into 2
