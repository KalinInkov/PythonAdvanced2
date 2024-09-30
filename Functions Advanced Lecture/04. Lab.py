def rectangle(length, width):
    def is_valid(a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return True
        else:
            return False

    if not is_valid(length, width):
        return f'"Enter valid values!"'

    def area(a, b):
        if is_valid(a, b):
            return a * b
        return False

    def perimeter(a, b):
        if is_valid(a, b):
            return 2 * (a + b)
        return False

    return f"Rectangle area: {area(length, width)}" + "\n" + \
           f"Rectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))
