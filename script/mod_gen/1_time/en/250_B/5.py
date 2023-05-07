def paint(n, a, b):
    for i in range(a):
        for j in range(b):
            if (i+j)%2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        for j in range(n-1):
            if (i+j)%2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
n, a, b = map(int, input().split())
for i in range(a):
    paint(n, a, b)
for i in range(n-1):
    paint(n, a, b)
I'm not sure what the problem is. I've tried to copy and paste the code from the editor and it works fine.
What's wrong with this code? I'm getting the correct output, but it's not accepted.
I'm getting the correct output, but it's not accepted.
That's because you're not printing the newlines. You're printing dots and hashes, but the problem statement says that you need to print newlines in between.
I'm getting the correct output, but it's not accepted.
That's because you're not printing the newlines. You're printing dots and hashes, but the problem statement says that you need to print newlines in between.
I'm sorry, I was looking at the wrong part of the code. I've fixed it now.
I'm sorry, I was looking at the wrong part of the code. I've fixed it now.
I'm not sure what the problem is. I've tried to copy and paste the code from the editor and it works fine.
I've tried to copy and paste the code from the editor and it works fine.
You should try to run your code locally. It's much easier to debug your code if you don't have to submit it every time.
You should try to run your code locally. It's much easier to debug your code if you don't have to submit it every time.
I've tried running it locally, but it still works fine. I'm not sure what the problem is.
I've tried running it locally, but it still works fine. I'm not sure what the problem is.
I've tried running it locally, but it still works fine.
That's because the sample inputs and outputs are small. Try running it with larger inputs. For example, try running it with N = 10, A = 10, and B =

if __name__ == '__main__':
    paint()