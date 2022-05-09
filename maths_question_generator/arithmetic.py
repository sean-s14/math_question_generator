import random
from .base import Base
from .utils import (
    eval_expression_mul_div, 
    pass_min_max, 
    generate_next_num, 
    factors, 
    generate_num_from_factors
)


class Arithmetic(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def basic(self) -> dict:
        """
        Returns a dictionary containing a question and an answer, both in string format.\n
        Example: `{"question": "7 * 6", "answer": "42"}`
        """

        def generate():
            numbers = []
            equation = []
            
            # Determine wether quantity is of type "list" or "int"
            quantity = self.quantity
            if type(self.quantity) == list:
                _ = random.randint(0, len(self.quantity) - 1)
                quantity = quantity[_]

            while len(numbers) < quantity:

                # ==================== Generate Number ====================
                if len(equation) > 1 and equation[-1] == '/':
                    # If doing division use factors of previous number to generate random number
                    answer = eval_expression_mul_div(equation)
                    num = generate_num_from_factors(answer)
                    attempts = 1
                    for _ in range(0, attempts):
                        if num == 1:
                            num = generate_num_from_factors(answer)
                else:
                    def generate_number(min_val, max_val):
                        """Generate random number between 2 specified values"""
                        
                        # 1 | Generate random number
                        if len(numbers) > 0: 
                            num = generate_next_num(min_val, max_val, numbers[-1])
                        else: 
                            num = generate_next_num(min_val, max_val)

                        # 2 | Find result of expression so far (only * and /)
                        answer = eval_expression_mul_div(equation + [str(num)])

                        # 3 | Check if answer passes min_eval and max_eval
                        eval_set = pass_min_max(int(answer), self.min_eval, self.max_eval)

                        # 4 | If answer does not pass re-generate random number
                        if eval_set is False:
                            num = generate_number(min_val, max_val - 1)
                            
                        return num

                    num = generate_number(self.min_val, self.max_val)
                            

                numbers.append(num)  # Keep track of number count
                equation.append(str(num))  # Convert to str to use join method later
                
                # ==================== Generate Operation ====================

                # Add operation if the last number in equation has not yet been added
                if len(numbers) < quantity:
                    # 1 | Get the result of the equation so far (only involving * and /)
                    answer = eval_expression_mul_div(equation)

                    # 2 | Create copy of operations list
                    operations = list(self.operations)

                    # 3 | If the number "0" is followed by division, change the operation
                    #     to avoid "ZeroDivisionError"
                    if  numbers[-1] == 0 or int(answer) == 0:
                        operations.remove('/')

                    # 4 | Reduce chances of 1 being followed by multiplication
                    if numbers[-1] == 1:
                        _ = random.randint(0, 1)  # 50% Chance
                        if _ == 0:
                            operations.remove('*')

                    # 5 | Find number of factors in expression thus far
                    if int(answer) != 0 and '/' in operations:
                        factor_count = len(list(factors(int(answer))))
                        # If there are only 2 factors in factor_count, reduce the 
                        #   chances of the next operation being division by 90%
                        if factor_count < 3:
                            coin_flip = random.randint(0, 9)  # 90% Chance of removing division 
                            if coin_flip != 0:
                                operations.remove('/')

                    # 6 | Choose operation at random
                    oper = random.choice(operations)
                    
                    # 7 | Add the operation to the equation
                    equation.append(oper)

            question = ' '.join(equation)
            answer = eval(question)

            return [question, answer]

        expression, answer = generate()
        match = pass_min_max(int(answer), self.min_res, self.max_res)

        while not match:
            expression, answer = generate()
            match = pass_min_max(int(answer), self.min_res, self.max_res)

        answer = str(int(answer))
        return {"question": expression, "answer": answer}