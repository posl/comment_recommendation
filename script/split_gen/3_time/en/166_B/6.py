def main():
    n, k = map(int, input().split())
    d = [int(input()) for _ in range(k)]
    a = [list(map(int, input().split())) for _ in range(k)]
    #print(n, k)
    #print(d)
    #print(a)
    for i in range(k):
        for j in range(d[i]):
            print(a[i][j])
main()
I am trying to make a program that will take in a list of numbers and then output the list in ascending order. I have tried to use a bubble sort but I am having trouble making the program work. I am a beginner and I am having trouble making the program work. The program will be used to sort a list of numbers that are inputted by the user.
import java.util.Scanner;
public class BubbleSort {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the length of the list: ");
        int length = input.nextInt();
        int[] list = new int[length];
        System.out.println("Enter the list: ");
        for (int i = 0; i < list.length; i++) {
            list[i] = input.nextInt();
        }
        int temp;
        for (int i = 0; i < list.length; i++) {
            for (int j = 0; j < list.length; j++) {
                if (list[i] < list[j]) {
                    temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
        System.out.println("The list in ascending order is: ");
        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i] + " ");
        }
    }
}
I am trying to make a program that will take in a list of numbers and then output the list in ascending order. I have tried to use a bubble sort but I am having trouble making the program work. I am a beginner and I am having trouble making the program work. The program will be used to sort a list of numbers that are inputted by the user.
import java.util.Scanner;
public class BubbleSort {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the length of the list: ");
        int length = input.nextInt
