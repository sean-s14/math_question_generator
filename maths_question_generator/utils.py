import random
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def generate_num_from_factors(n):
    """???"""
    return random.sample(list(factors(int(n))), 1)[0]


def eval_expression(expression):
    """
    Function to help enforce Bodmas

    Finds the final section of the expression that involves multiplication and/or division and evaluates it.

    If the last character in the string/list is an operator it is removed before evaluation. 
    
    Example input: `"7 + 4 * 6 / 3 / "`
    Evaluates: `"4 * 6 / 3"`
    Returns: `"8"`

    Parameters
    ---------
    expression : list, str
        An expression as either a list or string. 
        Example as string: `"7 + 4 * 6 / 3 /"` 
        Example as list: `["7", "+", "4", "*", "6", "/", "3", "/"]`

    Returns the result as a string
    """
    eq = expression

    # Change expression to a list if string
    if type(eq) == str:
        # If only 1 item in string return expression
        if " " not in eq: 
            return eq
        eq = eq.split()
    
    # Last Item
    print("eq :", eq)
    e = eq[-1]

    # Remove final operator
    if (e == '+') or (e == '-') or (e == '*') or (e == '/'):
        eq = eq[:-1]
    
    # If there's only one number then return the number
    if len(eq) == 1:
        return eq[0]

    # Reversing the list helps to find only the final parts of the expression
    eq = list(reversed(eq))

    # Set "eq" to equal only the final parts of an expression that involve multiplication and/or division 
    trimmed = False
    for x in eq:
        if trimmed == False:
            if x == '+':
                index = eq.index('+')
                eq = eq[:index]
                trimmed = True
            elif x == '-':
                index = eq.index('-')
                eq = eq[:index]
                trimmed = True

    eq = str(int(eval(" ".join(list(reversed(eq))))))
    return eq


def check_randomness(objects, min_val=0, max_val=100, min_res=0, max_res=100):
    """
    Checks the randomness of the answers provided in the `objects` parameter by finding 
    how many answers were above / below half of the `max_res`.
    
    Parameters
    ----------
    objects : list
        list of dictionaries containing a question and an answer
        Example: `[{'question': '22 + 4', 'answer': '26'}, {'question': '25 + 10', 'answer': '35'}]`
    max_val : int

    max_res : int
    
    """

    max_val = (max_val + min_val) // 2
    max_res = (max_res + min_res) // 2

    total_values = 0
    above_value = 0
    total_results = len(objects)
    above_result = 0
    for obj in objects:
        if int(obj['answer']) >= max_res:
            above_result += 1

        q = obj['question'].split()
        q = [a for a in q if (a != '+' and a != '-' and a != '*' and a != '/')]
        total_values += len(q)

        for num in q:
            if int(num) >= max_val:
                above_value += 1

    results = f"{int((above_result / total_results) * 100)}%"
    values= f"{int((above_value / total_values) * 100)}%"

    print('The below scores should be as close to 50% as possible for maximum randomness')
    return {'values': values, 'results': results}
    

def pass_min_max(answer, min_res, max_res):
    """
    Returns `True` if the answer generated is 
    more than `min_res` and less than `max_res` otherwise returns `False`
    """

    if min_res is None or max_res is None:
        return None

    if (min_res or (min_res == 0)) and (max_res or (max_res == 0)):
        while (answer < min_res) or (answer > max_res):
            return False
    elif min_res or (min_res == 0):
        while answer < min_res:
            return False
    elif max_res or (max_res == 0):
        while answer > max_res:
            return False

    return True


def swap_num_with_placeholder(placeholder, equation):
    """
    Takes a string or list and swaps a number in a list with the placeholder specified.
    Example Input: `("x", "1 + 3")`
    Example Output: `"1 + x"`, `"3"`
    """
    
    if type(equation) == str:
        equation = equation.split()

    num = True
    while num:
        choice_num = random.randint(0, len(equation)-1)
        choice_str = equation[choice_num]
        operations = ['+', '-', '*', '/']
        if choice_str not in operations:
            equation[choice_num] = placeholder
            placeholder_val = choice_str
            num = False

    return equation, placeholder_val


def convertListToStr(items: list or str) -> str:
    if type(items) == list:
        new_item = " ".join(items)
        return new_item
    elif type(items) == str:
        return items
    else:
        raise Exception("Value entered was not a string or a list")

def convertStrToList(string: str or list) -> list:
    if type(string) == str:
        if " " in string:
            return string.split()
        return [string]
    elif type(string) == list:
        return string
    else:
        raise Exception("Value entered was not a string or a list")


def generate_next_num(
    min_val: float, 
    max_val: float, 
    min_eval: float,
    max_eval: float,
    min_res: float,
    max_res: float,
    expression: list or str = None,
    prev_num: float = None,
    final: bool = False,
    chance: int = 100,
    ) -> int:
    """
    Returns a number that is higher/lower than prev_num based on the mean average of min_val and max_val.
    Example: `generate_next_num(5, 0, 20)`

    The mean average above is 10, and the previous number was 5, therefore the next number will be more than 10.
    Output: `12`

    Parameters
    ----------
    prev_num : float
        The last number in the expression
    min_val : float
        The minimum value generated
    max_val : float
        The maximum value generated
    chance : int
        An integer that represents the chance of the next value being above/below the mean average.
        Example: `chance=50` is equal to `50%`
    """

    # If this is the first number in the expression
    if prev_num is None:
        num = random.randint(min_val, max_val)
        return num
    
    # Create copy to not affect original expression
    expression = expression[:]

    if expression is None:
        raise Exception("No value was entered for expression in generate_next_num function")

    # Remove final operator if one exists
    # E.g. ["3", "+", "5", "*"] becomes ["3", "+", "5"]
    if any(item in ["+", "-", "*", "/"] for item in expression[-1]):
        # Get Last Item in Expression
        last_item: str = expression[-1]
        # Remove final operator
        expression = expression[:-1]
    else:
        raise Exception(f"No operation was found in the expression - {expression}")


    # Evaluate entire expression
    total_eval = int(eval(convertListToStr(expression)))
    # print("Total Evaluation of Expression :", total_eval)

    if last_item == "+":
        # Number could be above or below min_res/min_eval but not above max_eval
        # If final then Total will never exceed max_res either

        if total_eval <= max_eval:
            upper_bound = max_eval - total_eval
            upper_bound = max_val if upper_bound > max_val else upper_bound
            if final:
                if total_eval <= max_res:
                    upper_bound = max_res - total_eval
                    upper_bound = max_val if upper_bound > max_val else upper_bound
            num = random.randint(min_val, upper_bound)
        if upper_bound < 1: return 0
        num = random.randint(1, upper_bound)

    elif last_item == "-":
        # Number could be above or below max_res/max_eval but not above min_eval
        # If final then Total will never be less than min_res


        lower_bound = None

        if total_eval <= max_eval:
            # Check total_eval against min_eval & max_eval
            # E.g. total_eval= 47 or 60, max_eval=60, min_eval=1

            if final: # Last Number
                # Check total_eval against min_res & max_res
                if total_eval < max_res:
                    # E.g. total_eval=37, max_res=40, min_res=10
                    upper_bound = total_eval - min_res  # 27
                    upper_bound = max_val if upper_bound > max_val else upper_bound
                elif total_eval > max_res:
                    # E.g. total_eval=47, max_res=40, min_res=1
                    lower_bound = total_eval - max_res  # 7
                    upper_bound = total_eval - min_res  # 46
                    upper_bound = max_val if upper_bound > max_val else upper_bound
                else:
                    # E.g. total_eval=40, max_res=40
                    upper_bound = total_eval - min_eval
                    upper_bound = max_val if upper_bound > max_val else upper_bound
            else: # Not Last Number
                upper_bound = total_eval - min_eval  # 46
                upper_bound = max_val if upper_bound > max_val else upper_bound

        elif total_eval > max_eval:
            # E.g. total_eval=63, max_eval=60
            lower_bound = total_eval - max_eval  # 3
            upper_bound = total_eval - min_eval  # 62


        if lower_bound is None:
            num = random.randint(min_val, upper_bound)
        else:
            num = random.randint(lower_bound, upper_bound)

        return num

        if final:
            # Ensure that result of subtracted number is less than max_res 
            # E.g. total_eval=110, max_res=100, value=10, max_val=30, num_range=[10, 30]
            print("Total Evaluation :", total_eval)
            value = total_eval - max_res
            print("Total Evaluation - Max Result :", value)
            value = 1 if value < 1 else value

            # TODO: Ensure that result of subtracted number is more than min_res
            # E.g. total_eval=12, min_res=1, value=12, min_val=1, min_eval=1, num_range=[1, 11]
            value = total_eval - min_res


            num_range = [value, max_val]
            print("Number Range :", num_range)
        else:    
            # Ensure that subtracted number does not go below min_eval
            value = total_eval - min_eval
            num_range = [1, value]
        num = random.randint(*num_range)

    elif last_item == "*":
        # Ensure that the result of multipliying generated number does not exceed max_eval
        num = None
        _ = max_val
        count = 0  # To prevent potential endless loop
        # Repeat loop until num is not None
        while num is None:
            test_expression = None  # Reset test_expression
            test_num = random.randint(1, _)  # TODO: The 1 needs to be changed to min_val at some point
            print("Test Num :", test_num)
            test_expression = convertStrToList(expression.copy())
            test_expression.append(last_item)
            test_expression.append(str(test_num))
            test_expression = convertListToStr(test_expression)
            test_total_eval = float(eval(test_expression))
            if test_total_eval <= max_eval:
                if final and (test_total_eval <= max_res):
                    print("\nTest Expression :", test_expression)
                    print("Test Total Evaluation :", test_total_eval)
                    print("Max Result :", max_res)
                    print("Is Total less than Max Result?", test_total_eval <= max_eval)
                    print("Is Final :", final)
                    num = test_num
                else:
                    num = test_num
            # If number is too high then test_num becomes the highest number
            _ = test_num

            # To prevent potential endless loop
            count += 1
            if count > 20: return 1
    elif last_item == "/":
        # Ensure that the number generated is a factor of prev_num
        num = generate_num_from_factors(prev_num)
        # TODO: Do more stuff here, e.g. reduce chance of division of prime numbers etc.

    return str(num)

    # Create a list of 1's and 2's. 1's represent the chance specified as a parameter.
    chance_list = [ 1 for x in range(0, chance) ]
    while len(chance_list) < 100:
        chance_list.append(2)

    avg = (max_val + min_val) // 2
    below_avg = prev_num < avg
    
    if below_avg:
        # If the random number generated for "chance_num" corresponds with the number "1" then choose a 
        # number above the mean average of "min_val" and "max_val"
        if random.choice(chance_list) == 1:
            num = random.randint(avg, max_val)
        else:
            num = random.randint(min_val, avg-1)
    else:
        num = random.randint(min_val, max_val)

    return num


def generate_next_oper(
    min_res: float,
    max_res: float,
    expression: str or list = None,
    operations: list or str = ["+", "-", "*", "/"],
    negative: bool = False,
    ) -> str:
    """
    
    """
    operations = operations.copy()
    
    # TODO: If total eval is above max_res then remove addition and multiplication from operations
    # TODO: If total eval is below min_res then remove subtraction and division from operations

    if expression is None:
        raise Exception("No value was entered for expression in generate_next_num function")

    # Change expression to string if list
    if type(expression) == list:
        expression = " ".join(expression)

    # sub_exp_eval = result_of_final_sub_expression(expression)
    # print("Expression before eval :", expression)    
    total_eval = int(eval(convertListToStr(expression)))

    if (total_eval <= min_res):
        # E.g. total_eval= -10, min_res=0, operations=["+", "*"]
        if ("-" in operations):
            operations.remove('-')
        if ("/" in operations):
            operations.remove('/')
    elif (total_eval >= max_res):
        # E.g. total_eval= 100, max_res=80, operations=["-", "/"]
        if ("+" in operations):
            operations.remove('+')
        if ("*" in operations):
            operations.remove('*')

    # print("Operations :", operations)
    oper = random.choice(operations)



    return oper


def calcQty(qty: int or list) -> int:
    """Calculates the quantity of numbers to use"""

    # Choose number from list of quantities
    if type(qty) == list:
        qty = random.choice(qty)
    elif type(qty) != int:
        try:
            qty = int(qty)
        except Exception as e:
            print(e)
            return 2

    return qty


def result_of_final_sub_expression(
    expression: str or list,
    ) -> str :
    """
    - Function to help enforce Bodmas

    - Evaluates the last sub expression of a given expression and returns the outcome

    - Finds the final section of the expression that involves multiplication and/or division and evaluates it.

    If the last character in the string/list is an operator it is removed before evaluation. 
    
    Example input: `"7 + 4 * 6 / 3 / "`
    Evaluates: `"4 * 6 / 3"`
    Returns: `"8"`

    Parameters
    ---------
    expression : list, str
        An expression as either a list or string. 
        Example as string: `"7 + 4 * 6 / 3 /"` 
        Example as list: `["7", "+", "4", "*", "6", "/", "3", "/"]`

    Returns the result as a string
    """
    exp = expression

    # Change expression to a list if string
    if type(exp) == str:
        # If only 1 item in string return expression
        if " " not in exp: 
            return exp
        exp = exp.split()
    
    # Last Item
    # print("Last Item in Expression :", exp)
    e = exp[-1]

    # Remove final operator
    if (e == '+') or (e == '-') or (e == '*') or (e == '/'):
        exp = exp[:-1]
    
    # If there's only one number then return the number
    if len(exp) == 1:
        return exp[0]

    # Reversing the list helps to find only the final parts of the expression
    exp = list(reversed(exp))

    # Set "exp" to equal only the final parts of an expression that involve multiplication and/or division 
    trimmed = False
    for x in exp:
        if trimmed == False:
            if x == '+':
                index = exp.index('+')
                exp = exp[:index]
                trimmed = True
            elif x == '-':
                index = exp.index('-')
                exp = exp[:index]
                trimmed = True

    # Evaluate final sub expression
    exp = str(int(eval(" ".join(list(reversed(exp))))))
    return exp