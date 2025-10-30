def multiply_all(*args: int) ->int:
    prod = 1
    for arg in args:
        prod *= arg
    return prod

if __name__ == "__main__":
    print(multiply_all())
    print(multiply_all(2,3,4,5))
    print(multiply_all(3))
