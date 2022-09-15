class Step:
    """Keeps track of the current step.
    
    Attributes:
        __current_step (int): To keep track of the step of the message.
        __max_step (int): For the message to have a limit.
        __forward (bool): Keeps track of whether or not the message is going forward (Left to rigth).
    """

    def __init__(self, max_step = 5):
        """Constructs a  new Step
        
        Args:
            max_step (int): The furthest away the message can be on the left side of the terminal.
        """
        self.__currnet_step = 1
        self.__max_step = max_step
        self.__forward = True

    def advance(self):
        """Makes the message advance by 1"""
        self.__determine_direction()
        self.__currnet_step += 1 if self.__forward else -1
         
    def get_current_step(self):
        """Gets the current step.
        
        Returns:
            integer: The current step.
        """
        return self.__currnet_step

    def get_forward(self):
        """Gets forward value.
        
        Returns:
            boolean: Forward value.
        """
        return self.__forward

    def __determine_direction(self):
        """Updates the value for forward which determines in which direction the message will be going. 
           Forward (right) or backwards (left).
        """
        if self.__currnet_step == 1:
            self.__forward = True
        elif self.__currnet_step == self.__max_step:
            self.__forward = False

    
        
        
        


            
         

