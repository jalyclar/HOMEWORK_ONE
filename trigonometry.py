import sys 
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import ascii
import os 
import pandas as pd

#THINGS TO DEBGUG #####################################################################
#                                    NOTHING !
#######################################################################################


class homework_one:

    def __init__(self):
        self.function=None 
        self.filename=None
        self.read_from_file=None 
        self.print=None

        #Initialize certain things here instead of inside each function
        self.x=None #put np.arange here 
        self.y_values=None #make this a dict 
        self.y_list=None #make this an empty list maybe?
        self.table_df=pd.DataFrame
        
    def parse_argv(self): #Parsing over command line arguments 
        for argument in sys.argv[1:]: #Skips over 1st argument (script name)
            if argument.startswith("--function="): #Assigns after = 
                self.function=argument.split("=")[1]
            if argument.startswith("--write="):
                self.filename=argument.split("=")[1]
            if argument.startswith("--read_from_file="):
                self.read_from_file=argument.split("=")[1]
            if argument.startswith("--print="):
                self.print=argument.split("=")[1]
 
    def plot_func(self): #Plotting data from function(s) provided  
        if self.function==None: #Does nothing if function is not provided 
            print('Error: A function argument needs to be provided.')
            quit()

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
                print(f"Error: Function '{func}' is not understood.")
                quit()
            self.y_values[func]=y #stores y values and corresponding func in dict
            label=f'{func}(x)' 
            plt.plot(self.x,y,label=label)

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
                print("Error: No y values to put in table.") #If self.y_values werent passed correctly 
            data=[self.x] + [self.y_values[func].tolist() for func in self.y_values] #write function only takes lists or np.array
            names=['x']+ [f'{func}(x)' for func in self.y_values] 
            
            dir=os.path.dirname(os.getcwd()) #Stores in the parent directory outside the repository may not be neccessary
            file_path=os.path.join(dir,self.filename)

            ascii.write(data, file_path, names=names, overwrite=True) #Allows file to be overwritten 
            print(f'Data written to {file_path}')

    def read_file(self): #Reads and stores data from file 
        if self.read_from_file==None:
            pass #plot_from_file does nothing if no argument is given
        else:
            dir=os.path.dirname(os.getcwd()) #Reads from outside the repository but may not be needed 
            file_path=os.path.join(dir,self.read_from_file)
            
            #print(dir)
            #print(self.read_from_file)
            #print(file_path)
            self.table_df=pd.read_csv(file_path,delimiter=' ')
            print(self.table_df)

    def generate_plot(self):
        if self.print==None: #function does nothing if no argument is supplied 
            pass
        else:
            x=self.table_df.iloc[:,0] #x values assigned as first column in df
            for col in self.table_df.columns[1:]: 
                y=self.table_df[col] #y values assigned as each column after first 
                plt.plot(x,y,label=col)
            plt.title(f"Plot of {' , '.join([f'{col}' for col in self.table_df.columns[1:]])}") 
            plt.xlabel("x values")
            plt.ylabel(f"{' , '.join([f'{col}' for col in self.table_df.columns[1:]])}")
            plt.legend()
            plt.show() #Comment out for final commit  

            format=self.print.split(",") #Splits provided arguments if provided multiple 
            dir=os.path.dirname(os.getcwd()) #Will save file to directory above this one (outside repository)
            name='exampleplot.' #Name given to file that will have the plot(s) 
            for option in format:
                if option=='jpeg':
                    full=''.join([name,option])#joins together filename and format provided 
                    plt.savefig(os.path.join(dir,full))
                elif option=='eps':
                    full=''.join([name,option])
                    plt.savefig(os.path.join(dir,full))
                elif option=='pdf':
                    full=''.join([name,option])
                    plt.savefig(os.path.join(dir,full))
                else:
                    print(f'Error: {option} not understood')
                    continue
            print(f"Plots saved as 'exampleplot' in the following formats: {[option for option in format]}") #Lists all the formats its saved as
                #print(full)
            #plt.show()

if __name__ == "__main__": #Allows script to be ran within command line 
    data=homework_one() #Calls all functions from within the class for command line 
    data.parse_argv()
    data.plot_func()
    data.write_file()
    data.read_file()
    data.generate_plot()