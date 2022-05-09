class Base:

    def __init__(
        self,
        opers: list = ['add', 'sub', 'mul', 'div'],
        min_val: float = 0,
        max_val: float = 100,
        min_eval: float = 0,
        max_eval: float = None,
        min_res: float = 0,
        max_res: float = None,
        quantity: int or list = [2, 3],
        difficulty: str or list = None
        # TODO: decimals: bool = False,
        # TODO: decimal_place: int = 1,
        ):
        """
        Parameters
        ----------
        opers : list
            A list of operations to include in the equations.
            Options are `add`, `sub`, `mul` & `div`.
        min_val : float
            The lowest number to be used in the equation
        max_val : float
            The highest number to be used in the equation
        min_eval : float
            The lowest number that can be evaluated at any stage in the equation
        max_eval : float
            The highest number that can be evaluated at any stage in the equation
        min_res : float
            The lowest number to be output by the equation
        max_res : float
            The highest number to be output by the equation
        quantity : int or list
            The quantity of numbers used in the equation
        difficulty : str or list
            The difficulty of the questions. This overrides all other parameters.
        """

        self.opers = opers
        self.min_val = min_val
        self.max_val = max_val
        self.min_eval = min_eval
        self.max_eval = max_eval
        self.min_res = min_res
        self.max_res = max_res
        self.quantity = quantity
        self.difficulty = difficulty

        error_messages = {
            "quantityLow": "Quantity is too low. Choose a number above 1",
            "quantityHigh": "Quantity is too high. Choose a number below 7",
            "wrongType": "The value you entered is not of the correct type"
        }

        if type(quantity) == list:
            for n in quantity:
                if   n < 2: raise ValueError(error_messages["quantityLow"])
                elif n > 6: raise ValueError(error_messages["quantityHigh"])
        elif type(quantity) == int:
            if   quantity < 2: raise ValueError(error_messages["quantityLow"])
            elif quantity > 6: raise ValueError(error_messages["quantityHigh"])
        else:
            raise TypeError(error_messages["wrongType"])

        self.operations = []
        self.operations.append('+') if 'add' in self.opers else None
        self.operations.append('-') if 'sub' in self.opers else None
        self.operations.append('*') if 'mul' in self.opers else None
        self.operations.append('/') if 'div' in self.opers else None

