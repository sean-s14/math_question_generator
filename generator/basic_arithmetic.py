import random
from functools import reduce

def basic_arithmetic(
    add: bool = True,
    sub: bool = True,
    mul: bool = True,
    div: bool = True,
    min: float = 0,
    max: float = 100,
    min_res: float = None,
    max_res: float = None,
    quantity: int = 2,
    # decimals: bool = False,
    # decimal_place: int = 1,
    ) -> object:
    """
    Parameters
    ----------
    add, sub, mul, div : bool
        Booleans that determines if the specified operation should be used in the equation.
    quantity : int
        The amount of numbers used in the equation
    min : float
        The lowest number to be used in the equation
    max : float
        The highest number to be used in the equation
    min_res : float
        The lowest number to be output by the equation
    max_res : float
        The highest number to be output by the equation

    Returns
    -------
    A dictionary with a question and an answer, both in string format.\n
    Example:\n
    {
        "question": "5 + 5", 
        "answer": "10"
    }
    """

    def factors(n):    
        return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    operations = []
    operations.append('+') if add else None
    operations.append('-') if sub else None
    operations.append('*') if mul else None
    operations.append('/') if div else None


    def generate():
        numbers = []
        equation = []
        
        while len(numbers) < quantity:

            # If doing division ensure result of calculation is integer
            if len(equation) > 1 and equation[-1] == '/':
                num = random.sample(list(factors(int(equation[-2]))), 1)[0]
            else:
                num = random.randint(min, max)

            numbers.append(num)  # Keep track of number count
            equation.append(str(num))  # Convert to str to use join method later
            
            if len(numbers) < quantity:  # Don't add operation after last number
                oper = random.randint(0, len(operations)-1)
                while (numbers[-1] == 0) and (operations[oper] == '/'):
                    oper = random.randint(0, len(operations)-1)
                equation.append(operations[oper])


        question = ' '.join(equation)
        answer = int(eval(question))
        return {"question": question, "answer": answer}

    q_and_a = generate()

    if (min_res or (min_res == 0)) and (max_res or (max_res == 0)):
        while (q_and_a["answer"] < min_res) or (q_and_a["answer"] > max_res) :
            q_and_a = generate()
    elif min_res or (min_res == 0):
        while q_and_a["answer"] < min_res:
            q_and_a = generate()
    elif max_res or (max_res == 0):
        while q_and_a["answer"] > max_res:
            q_and_a = generate()

    return q_and_a

if __name__ == "__main__":
    basic_arithmetic()