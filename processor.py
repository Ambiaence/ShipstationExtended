class Processor:
    def __init__(self, process_function):
        if not callable(process_function): 
            t = str(type(process_function))
            raise Exception("Class Processor must be contructed with a function, but the type is " + t)

        orders = dict()
