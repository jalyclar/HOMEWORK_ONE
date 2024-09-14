import sys 
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import ascii
import os 
import pandas as pd

class homework_one:

    def __innit__(self):
         
        self.function=None 
        self.filename=None
        self.read_from_file=None 
        self.print=None

        #Initialize certain things here instead of inside each function
        self.x=None #put np.arange here 
        self.y_values=None #make this a dict 
        self.y_list=None #make this an empty list maybe?
        
    def parse_arguments(self): #Parsing over command line arguments 
        for argument in sys.argv[1:]:
            if argument.startswith("--function="): #Assigns after = 
                self.function=argument.split("=")[1]
            if argument.startswith("--write="):
                self.filename=argument.split("=")[1]
            if argument.startswith("--read_from_file="):
                self.read_from_file=argument.split("=")[1]
            if argument.startswith("--print="):
                self.print=argument.split("=")[1]
 
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
            self.y_values[func]=y #stores y values and corresponding func in dict 
            plt.plot(self.x,y,label=func)

        plt.title(f"Plot of {' , '.join([f'{f}(x)' for f in functions])}")
        plt.xlabel("x values")
        plt.ylabel(f"{' , '.join([f'{f}(x)' for f in functions])}")
        plt.legend()
        plt.show()
    
    def write_file(self): 
        if self.filename==None:
            pass #write_file does nothing if no argument is given 
        else:
            if self.y_values is None:
                print("No y values to put in table.") #If self.y_values werent passed correctly 
            data=[self.x] + [self.y_values[func].tolist() for func in self.y_values] #write function only takes lists or np.array
            names=['x']+ [f'{func}(x)' for func in self.y_values] 
            
            dir=os.path.dirname(os.getcwd()) #Stores in the parent directory outside the repository may not be neccessary
            file_path=os.path.join(dir,self.filename)

            ascii.write(data, file_path, names=names, overwrite=True) #Allows file to be overwritten 
            print(f'Data written to {file_path}')

    def plot_from_file(self):
        if self.read_from_file==None:
            pass #plot_from_file does nothing if no argument is given
        else:
            #print(type(self.read_from_file))
            
            dir=os.path.dirname(os.getcwd()) #Reads from outside the repository but may not be needed 
            file_path=os.path.join(dir,self.read_from_file)
            
            #print(dir)
            #print(self.read_from_file)
            #print(file_path)
            data=pd.read_csv(file_path,delimiter=' ')
            print(data)

if __name__ == "__main__": #Allows script to be ran within command line 
    data=homework_one()
    data.parse_arguments()
    data.plot_func()
    data.write_file()
    data.plot_from_file()

    
