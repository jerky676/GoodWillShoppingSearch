from enum import Enum,unique
import enum

class QueryItem:
    def __init__(self, query_string: str, value):
        self.query_string = query_string
        self.value_set(value)

    def query_string_value(self):
        return f'{self.query_string}={self.get_value()}'
   
    def query_string(self):
        return self.query_string
        
    def value_set(self, query_value):
        if type(query_value) is Enum:
            print(f'this is an enum')
        self.query_value = query_value

    def get_value(self):
        if type(self.query_value) is str:
            return self.query_value.lower()
        elif isinstance(self.query_value,enum.Enum):
            return str(self.query_value.value)
        else:          
            return str(self.query_value).lower()