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
        return self.value