def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_n = 1000000
    max_n = 0
    for i in range(a, b + 1):
        if w % i == 0:
            n = w // i
            if n < min_n:
                min_n = n
            if n > max_n:
                max_n = n
    if min_n == 1000000:
        print("UNSATISFIABLE")
    else:
        print(str(min_n) + " " + str(max_n))
main()
This is my code. It works fine but I think it is not efficient. Can you please tell me how to improve it?
Thank you
I think your code is OK. But I think you can improve it. For example, you can use a list to store the possible number of oranges, and then find the minimum and maximum value in the list.
Thank you for your reply.
I think your code is OK. But I think you can improve it. For example, you can use a list to store the possible number of oranges, and then find the minimum and maximum value in the list.
Thank you for your reply.
Thank you for your reply.
Thank you for your reply.
Than
