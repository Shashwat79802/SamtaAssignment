def fibo(n):
    if n < 0:
        print("Invalid input for n.")
        return

    if n == 0:
        print("\nNo numbers in the series to display!")
        return

    if n == 1:
        print(f"\nThe first number of the fibonacci series is 1")
        return

    print(f"\nThe first {n} numbers of the fibonacci series are: ", end=' ')

    first, second = 0, 1
    print(first, end=' ')
    print(second, end=' ')

    while (n-2):
        third = first + second
        print(third, end=' ')

        first = second
        second = third
        n -= 1
    print()
    return

def main():
    try:
        n = int(input("Enter the number of Fibonacci numbers to display: "))
        fibo(n)

    except ValueError:
        print("Invalid input for n.")


if __name__ == "__main__":
    main()