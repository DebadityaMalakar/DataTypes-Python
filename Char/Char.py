class  Char:
    """
    Char datatype is same as the char in C.
    """
    def __init__(self,x,mln):
        self.x=x
        self.mln=mln
        try:
            self.x=self.x[:self.mln]
        except TypeError:
            self.x=str(self.x)
            self.x=self.x[:self.mln]
    def __str__(self):
        return f"{self.x}"
    def __repr__(self):
        return f"{self.x}"
