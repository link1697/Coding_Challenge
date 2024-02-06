class Error(Exception):
        def __init__(self, id, value):
            self.id = id
            self.value = value

class Operation:
    def list_modify(numList):
        if len(numList) % 10 != 0:
            raise Error(0, 'Error: The length of the list is {}, not a multiple of 10.'.format(len(numList)))
            
        resList = [num for i, num in enumerate(numList) if (i+1) % 2 != 0 and (i+1) % 3 != 0]
        return resList