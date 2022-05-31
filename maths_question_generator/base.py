class Base:

    def __init__(
        self,
        opers: list = ["+", "-", "*", "/"],
        min_val: float = 1,
        max_val: float = 100,
        min_eval: float = 1,
        max_eval: float = 200,
        min_res: float = 1,
        max_res: float = 200,
        quantity: int or list = [2, 3],
        difficulty: str or list = None,
        negative: bool = False,
        decimals: bool = False,
        decimal_place: int = 1,
        ):
        """
        Parameters
        ----------
        opers : list
            A list of operations to include in the equations.
            Options are `+`, `-`, `*` & `/`.
        min_val : float
            The lowest number to be used in the equation
        max_val : float
            The highest number to be used in the equation
        min_eval : float
            The lowest number that the expression can be evaluated to at any stage in the equation
        max_eval : float
            The highest number that the expression can be evaluated to at any stage in the equation
        min_res : float
            The lowest number to be output by the equation
        max_res : float
            The highest number to be output by the equation
        quantity : int or list
            The quantity of numbers used in the equation. Must be more than 1 and less than 7
        difficulty : str or list
            The difficulty of the questions. This overrides all other parameters.
        negative : bool
            Wether or not the values used or the value at any stage will be negative
        """

        error_messages = {
            "quantityLow": "Quantity is too low. Choose a number above 1",
            "quantityHigh": "Quantity is too high. Choose a number below 7",
            "wrongType": "The value you entered is not of the correct type"
        }

        # Ensures that quantity is above 1 but below 7
        if type(quantity) == list:
            for n in quantity:
                if   n < 2: raise ValueError(error_messages["quantityLow"])
                elif n > 6: raise ValueError(error_messages["quantityHigh"])
        elif type(quantity) == int:
            if   quantity < 2: raise ValueError(error_messages["quantityLow"])
            elif quantity > 6: raise ValueError(error_messages["quantityHigh"])
        else:
            raise TypeError(error_messages["wrongType"])


        self.difficulty = difficulty
        self.min_val = min_val
        self.min_eval = min_eval
        self.min_res = min_res
        self.negative = negative
        self.decimals = decimals
        self.decimal_place = decimal_place

        if difficulty is None:
            self.operations = opers
            self.max_val = max_val
            self.max_eval = max_eval
            self.max_res = max_res
            self.quantity = quantity
        elif difficulty == "easy":
            self.operations = ["+", "-"]
            self.max_val = 20
            self.max_eval = 60
            # self.min_res = -20
            self.max_res = 40
            self.quantity = quantity
        elif difficulty == "normal":
            self.operations = ["+", "-", "*"] #, "/"]
            self.max_val = 40
            self.max_eval = 120
            # self.min_res = -40
            self.max_res = 80
            self.quantity = [2, 3, 4]
            # self.quantity = 4
        elif difficulty == "hard":
            self.operations = ["+", "-", "*"] #, "/"]
            self.min_val = min_val  # TODO: -60
            self.max_val = 60
            self.min_eval = min_eval  # TODO: -180
            self.max_eval = 180
            self.min_res = min_res  # TODO: -120
            # self.min_res = -60
            self.max_res = 120
            self.quantity = [3, 4, 5]
            # TODO: Enable the below attribues
            self.negative = negative  # True
            self.decimals = decimals  # True

        # print(
        #     "\n====================\nDifficulty :", 
        #     self.difficulty[0].upper() + self.difficulty[1:],
        #     '\n--------------------',
        #     "\nMax Value :", self.max_val,
        #     "| Max Evaluation :", self.max_eval,
        #     "| Max Result :", self.max_res
        # )
