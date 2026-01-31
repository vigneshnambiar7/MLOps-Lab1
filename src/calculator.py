def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x, y, z):
    """
    Performs multiple operations and returns the result.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Result of (x + y) * z.
    """
    addition = fun1(x, y)
    result = fun3(addition, z)
    return result

def fun5(x, y):
    """
    Divides two numbers.
    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.
    Returns:
        float: Quotient of x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def fun6(x, y):
    """
    Calculates x raised to the power of y.
    Args:
        x (int/float): Base number.
        y (int/float): Exponent.
    Returns:
        int/float: x raised to power y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y

def fun7(numbers):
    """
    Calculates the average of a list of numbers.
    Args:
        numbers (list): List of numbers.
    Returns:
        float: Average of the numbers.
    Raises:
        ValueError: If list is empty or contains non-numeric values.
    """
    if not numbers:
        raise ValueError("List cannot be empty.")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements must be numbers.")
    return sum(numbers) / len(numbers)


f1_op = fun1(2,3)
f2_op = fun2(2,3)
f3_op = fun3(2,3)
f4_op = fun4(f1_op,f2_op,f3_op)

print(f"fun1(2,3) = {f1_op}")
print(f"fun2(2,3) = {f2_op}")
print(f"fun3(2,3) = {f3_op}")
print(f"fun4({f1_op},{f2_op},{f3_op}) = {f4_op}")

