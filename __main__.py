from classes.Message import Message
from classes.Step import Step

def main():

    step = Step()
    message = Message(step)

    while True:
        message.display()

if __name__ == "__main__":
    main()  

    
