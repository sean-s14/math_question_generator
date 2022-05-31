import random
from .base import Base
from .utils import (
    eval_expression, 
    pass_min_max, 
    factors, 
    generate_num_from_factors,
    generate_next_num, 
    generate_next_oper,
    calcQty,
    result_of_final_sub_expression,
    convertListToStr,
    convertStrToList,
)


class Arithmetic(Base):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def base(self) -> dict:
        numbers = []
        expression = []

        qty = calcQty(self.quantity)

        while len(numbers) < qty:
            # Generate first number
            if len(numbers) == 0:
                # print("Generating first number...")
                next_num = generate_next_num(
                    self.min_val, self.max_val, 
                    self.min_eval, self.max_eval,
                    self.min_res, self.max_res,
                )
            elif len(numbers) == qty -1: # Generate last number
                prev_result = result_of_final_sub_expression(expression)
                next_num = generate_next_num(
                    self.min_val, self.max_val, 
                    self.min_eval, self.max_eval, 
                    self.min_res, self.max_res,
                    expression, prev_result,
                    final=True,
                )
            else: # Generate Next Number
                prev_result = result_of_final_sub_expression(expression)
                next_num = generate_next_num(
                    self.min_val, self.max_val,
                    self.min_eval, self.max_eval,
                    self.min_res, self.max_res,
                    expression, prev_result,
                )
            
            numbers.append(next_num)
            expression.append(str(next_num))

            # If last number added then break
            if len(numbers) == qty: break

            # Add Next Operation
            operation = generate_next_oper(
                self.max_val, self.min_res, self.max_res, 
                qty=qty - len(numbers),
                expression=expression,
                operations=self.operations,
                negative=self.negative
            )
            expression.append(operation)

        answer = int(eval(convertListToStr(expression)))

        dic = {}
        dic["question"] = convertListToStr(expression)
        dic["answer"] = str(answer)
        # print(dic)
        return dic

        # TESTING
        for number in numbers:
            if int(number) < self.min_val:
                raise Exception("One of the values generated was too low!") 
            if int(number) > self.max_val:
                raise Exception("One of the values generated was too high!") 

        if answer < self.min_res:
            raise Exception("Answer is too low!")
        if answer > self.max_res:
            raise Exception("Answer is too high!")

        return dic

