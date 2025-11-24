class Database():
    def __init__(self,sql_query):
        self.sql_query = sql_query
        if not self.sql_query.__len__():
            print("SQL query is not set")

