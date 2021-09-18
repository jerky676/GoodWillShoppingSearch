from enum import Enum,unique

class QueryItem:
    def __init__(self, query_string: str, value: str):
        self.query_string = query_string
        self.value = value

    def query_string_value(self):
        return f'{self.query_string}={self.value}'
   
    def query_string(self):
        return self.query_string
        
    def value_set(self, value: str):
        self.value = value

    def value(self):
        if type(self.value) is str:
            print(f'THIS IS AN STRING')
            return self.value
        elif type(self.value) is Enum:
            print(f'THIS IS AN ENUM')
            return self.value.value