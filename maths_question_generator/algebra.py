import random
from .base import Base
from .arithmetic import Arithmetic
from .utils import (
    eval_expression, 
    pass_min_max,
    swap_num_with_placeholder,
)


class Algebra(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def linear_algebra(self, placeholders='x') -> dict:
        # TODO: Add parameter for selection of letters to be used as placeholders in equations
        """
        Returns a dictionary containing a question (as a linear equation) and an answer.\n
        Example: `{"question": "x + 5 = 10", "answer": "5"}`

        Parameters
        ----------
        placeholders : list or str

        """

        if type(placeholders) == str:
            placeholders = [placeholders]
        placeholder = random.choice(placeholders)

        def generate():
            # print('a |', a)
            a_res = a.basic()
            # print('a_res |', a_res)
            question = a_res['question'].split()
            # print('question |', question)
            question, answer = swap_num_with_placeholder(placeholder, question)
            # print('question |', question, '| answer |', answer)
            question = " ".join(question)
            # TODO: Alternate between displaying "expression first then answer" and "answer first then expression"
            equation = f"{question} = {a_res['answer']}"
            return [equation, answer]

        difficulty = None
        try:
            difficulty = self.args[9]
        except IndexError as e:
            # print(e)
            pass
        
        if difficulty is None:
            try:
                difficulty = self.kwargs['difficulty']
            except KeyError as e:
                # print(e)
                pass
        # print(difficulty)

        if type(difficulty) == list:
            # print('Choosing difficulty...')
            difficulty = random.choice(difficulty)

        if difficulty == 'easy':
            # print('difficulty is easy')
            a = Arithmetic(max_val=20, max_eval=50, max_res=30)
        elif difficulty == 'normal':
            a = Arithmetic(
                min_val=-20, max_val=40, min_eval=-50, max_eval=100, 
                min_res=-30, max_res=60, quantity=3)
        elif difficulty == 'hard':
            a = Arithmetic(
                min_val=-40, max_val=80, min_eval=-100, max_eval=200, 
                min_res=-60, max_res=120, quantity=4)
        else:
            a = Arithmetic(*self.args, **self.kwargs)

        # print(a)
        equation, answer = generate()
        return {"question": equation, "answer": answer}