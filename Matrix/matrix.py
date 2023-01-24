class Matrix():
    def __init__(self,rows,cols,*row):
        self.matrix=[]
        self.rows=rows;
        self.cols=cols;
        self.row=row;
        if len(row) == self.rows:
            for i in row:
                if len(i) > self.cols:
                    print(f"No of columns cannot be more than {self.cols}")
                else:
                    self.matrix.append(list(map(int,i)))
        else:
            print(f"No of rows can be more than {self.rows}.")
        # firstrow=list(map(int,self.row))
        # self.matrix.append(firstrow)
        # secondrow=list(map(int,self.col))
        # self.matrix.append(self.col)
    def __str__(self):
        return f"{self.matrix}"
    def __repr__(self):
        return f"{self.matrix}"
