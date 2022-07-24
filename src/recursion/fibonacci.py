
def fibonacci(n):
    if n < 1:
        raise ValueError("The fibonacci series does not accept negative inputs. f(0) = f(-1)+f(-2)")
    elif n < 3:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(f"The 5th number of the Fibonacci series is {fibonacci(5)}!")
    print(f"The 10th number of the Fibonacci series is {fibonacci(10)}!")