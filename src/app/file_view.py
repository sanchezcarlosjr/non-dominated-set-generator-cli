class FileView:
    def __init__(self, file, pareto_front):
        self.file = file
        self.pareto_front = [" ".join(row) for row in pareto_front.astype(str)]
        self.rows = pareto_front.shape[0]
        self.columns = pareto_front.shape[1]
        if self.rows == 0 or self.columns == 0:
            raise Exception("Your parameters has generated an invalid space. Try to decrease translation.")

    def make(self):
        with open(f"{self.file}", "w") as file:
            file.write(f"# {self.rows} {self.columns} \n")
            for row in self.pareto_front:
                file.write(f"{row} \n")


