//上底の長さが a、下底の長さが b、高さが h の台形があります。
//この台形の面積を求めてください。
//1≤a≤100
//1≤b≤100
//1≤h≤100
//入力で与えられる値はすべて整数
//h は偶数
//入力例1
//3
//4
//2
//出力例1
//7

import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int h = sc.nextInt();
        System.out.println((a + b) * h / 2);
    }
}