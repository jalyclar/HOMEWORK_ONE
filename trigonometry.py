import sys 
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import ascii

class homework_one:

    def __innit__(self):
        #These are being repeated remove from here at some point !!!
        self.function=None 
        self.filename=None
        self.x=None
        self.y_values=None 
        self.y_list=None 
        #self.read_from_file=None 
        #self.print=None
    

    #Parsing over command line arguments 
    def parse_arguments(self):
        for argument in sys.argv:
            if argument.startswith("--function="): #Assigns after = 
                self.function=argument.split("=")[1]
            #Making these optional so no error is thrown 
            if argument.startswith("--write="):
                self.filename=argument.split("=")[1]
            else:
                self.filename=None
            if argument.startswith("--read_from_file="):
                self.read_from_file=argument.split("=")[1]
            else:
                self.read_from_file=None
            if argument.startswith("--print="):
                self.print=argument.split("=")[1]
            else:
                self.print=None 
 
    def plot_func(self):

        if self.function is None:
            print('No function understood.')

        self.x=np.arange(-10,10,0.05)
        self.y_values={}
    
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

        plt.title(f"Plot of {' , '.join([f'{f}(x)' for f in functions])}")
        plt.xlabel("x values")
        plt.ylabel(f"{' , '.join([f'{f}(x)' for f in functions])}")
        plt.legend()
        plt.show()
    
    def write_file(self):
        if self.filename==None:
            pass
        else:
            if self.y_values is None:
                print("No y values to put in table.")
            data=[self.x] + [self.y_values[func].tolist() for func in self.y_values]
            names=['x']+ [f'{func}(x)' for func in self.y_values]
            ascii.write(data, self.filename, names=names)
            print(f'Data written to {self.filename}')
            #Add in something to allow overwriting the file if already created !!!!
    
if __name__ == "__main__":
    data=homework_one()
    data.parse_arguments()
    data.plot_func()
    data.write_file()

    
