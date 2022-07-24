
def factorial(n):
    if n < 0:
        raise ValueError("Factorial does not accept negative integers!")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(f"Factorial of 5 is {factorial(5)}!")
    print(f"Factorial of 10 is {factorial(10)}!")
