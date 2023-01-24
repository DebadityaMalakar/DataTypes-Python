from bitstring import BitArray,CreationError

class Int2(int):
    """
    Helps to create a Integer of 2bits i.e from 0 to 3.
    """
    def __init__(self,x=0):
        self.x=BitArray(2)
        try:
            self.x.uint=int(x)
        except CreationError:
            self.x.uint=0
    def __str__(self) -> str:
        return f"{self.x.uint}"
    def __repr__(self):
        return f"{self.x.uint}"
    def __len__(self):
        return f"{len(str(self.x.uint))}"
    def replace(self,pos,value):
        z=""
        y=self.x.uint
        y=list(str(y))
        try:
            y[pos]=value
        except IndexError:
            return f"Index {pos} Not Found"
        for i in y:
            z += str(i)
        z=int(z)
        self.x.uint=int(z)
        return z
