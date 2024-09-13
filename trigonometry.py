import sys 
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import ascii

class homework_one:

    def __innit__(self):
        self.function=None 
        self.write=None 
        self.read_from_file=None 
        self.print=None
        self.x=None
        self._values={}

    #Parsing over command line arguments 
    def parse_arguments(self):
        for argument in sys.argv:
            if argument.startswith("--function="): #Assigns after = 
                self.function=argument.split("=")[1]
            if argument.startswith("--write="):
                self.write=argument.split("=")[1]
            if argument.startswith("--read_from_file="):
                self.read_from_file=argument.split("=")[1]
            if argument.startswith("--print="):
                self.print=argument.split("=")[1]
        return self.function, self.write, self.read_from_file, self.print
 
    def plot_func(self):
        self.x=np.arange(-10,10,0.05)
    
        functions=self.function.split(",") #Seperates multiples func if given 
        for func in functions:
            if func == "cos":
                y=np.cos(self.x)
            elif func == "sin":
                y=np.sin(self.x)
            elif func == "sinc":
                y=np.sinc(self.x)
            else:
                print(f"Function {func} is not understood.")
                continue #Skips over bad inputs 
            self.y_values[func]=y
            plt.plot(self.x,y,label=func)

        plt.title(f"Plot of {' (x),  (x)'.join([f'{f}(x)' for f in functions])}")
        plt.xlabel("x values")
        plt.ylabel(f"{' (x),  (x)'.join([f'{f}(x)' for f in functions])}")
        plt.legend()
        plt.show()
    
    def write_file(self):
        ascii.write([self.x,[self.y_values[func] for func in self.y_values]], self.write, names=['x',(f'{func}(x)' for func in self.y_values)])
        print(f'Data written to {self.write}')
    