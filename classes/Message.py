from email import message
from classes.Step import Step
from time import sleep as zzz

class Message:
    """A message that gets displau on the terminal.

    Attributes:
        __message (string): The message is diplayed on screen.
        __step (Step): The step or position the message is at.

    """
    def __init__(self, step, time_asleep = 0.3, message = "Hello World"):
        """Contructs a new Message.
        
        Args:
            step (Step): An instance of Step.
            message (string): The message that will be displayed.
        """

        self.__message = message
        self.__step = step
        self.__time_asleep = time_asleep

    
    def display(self):
        """Displays the message with the specifed number of tabs every 0.5 seconds"""
        zzz(self.__time_asleep)
        print("\t" * self.__step.get_current_step(), self.__message)
        self.__step.advance()
    



