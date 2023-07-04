from typing import Generic, TypeVar


INPUT_TYPE = TypeVar("INPUT_TYPE")
OUTPUT_TYPE = TypeVar("OUTPUT_TYPE")

class TaskBaseRequest(Generic[INPUT_TYPE, OUTPUT_TYPE]):
    def __init__(self):
        raise NotImplementedError("This class is not meant to be instantiated.")
    
    def request(self, input: INPUT_TYPE) -> OUTPUT_TYPE:
        raise NotImplementedError("This method is not meant to be called.")
