def calculator(num1, num2, operator):
    """
    name: calculator 
    Description: Performs basic arithmetic operations.
    Function: calculator(num1, num2, operator)
    Args: 
        - num1 (str or int): The first number.
        - num2 (str or int): The second number.
        - operator (str): The operator to perform ('+', '-', '*', '/', '%', '**').
    Returns: result of the calculation as string.

    Example action for using this tool:
    {"key": "action","content": {"tool": "calculator", "args": {"num1": 125, "num2": 165, "operator": "*"}}}
    """
    try:
        num1 = float(num1)  # Allow decimal inputs
        num2 = float(num2)

        if operator == "+":
            result = num1 + num2
            operation = "addition"
        elif operator == "-":
            result = num1 - num2
            operation = "subtraction"
        elif operator == "*":
            result = num1 * num2
            operation = "multiplication"
        elif operator == "/":
            if num2 == 0:
                return f"result from tool: None, message: Error: Division by zero"
            result = num1 / num2
            operation = "division"
        elif operator == "%":
            result = num1 % num2
            operation = "modulus"
        elif operator == "**":
            result = num1 ** num2
            operation = "exponentiation"
        else:
            return f"result from tool: None, message: Invalid operator"

        return f"result from tool: {result}, message: The result of {num1} {operation} {num2} is: {result}"

    except ValueError:
        return f"result from tool: None, message: Invalid input: please enter valid numbers."
