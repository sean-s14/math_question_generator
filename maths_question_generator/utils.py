import random
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def generate_num_from_factors(n):
    return random.sample(list(factors(int(n))), 1)[0]


# This is used to enlarge range of factors used for division
def eval_expression_mul_div(equation):
    """
    Finds the final section of the expression that involves multiplication and/or division and evaluates it.

    If the last character in the string/list is an operator it is removed before evaluation. 
    
    Example input: `"7 + 4 * 6 / 3 / "`
    Evaluates: `"4 * 6 / 3"`
    Returns: `"8"`

    Paramters
    ---------
    equation : list, str
        An equation as either a list or string. 
        Example as string: `"7 + 4 * 6 / 3 /"` 
        Example as list: `["7", "+", "4", "*", "6", "/", "3", "/"]`

    Returns the result as a string
    """
    eq = equation

    if type(eq) == str:
        eq = eq.split()
    
    # Last Item
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


def generate_next_num(min_val: float, max_val: float, prev_num: float = None, chance: int = 100):
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
    
    if prev_num is None:
        num = random.randint(min_val, max_val)
        return num

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