#phony targets 
.PHONY: run plot write read

#flags which correspond to command line arguments 
SCRIPT=./trigonometry.py
FXN ?=
TXT=filename.txt
FMT ?=

#Only plots provided function 
plot:
	$(SCRIPT) --function=$(FXN)

#Plots and writes to a file  
write:
	$(SCRIPT) --function=$(FXN) --write=$(TXT)

#Plots, writes to a file, and reads the file to produce a plot 
read: 
	$(SCRIPT) --function=$(FXN) --write=$(TXT) --read_from_file=$(TXT)

#Does all the functions from the script  
run:
	$(SCRIPT) --function=$(FXN) --write=$(TXT) --read_from_file=$(TXT) --print=$(FMT)
