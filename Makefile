#phony targets 
.PHONY: run plot write read

#flags which correspond to arguments 
SCRIPT=./trigonometry.py
FXN ?=
TXT=filename.txt
FMT ?=
 
run: plot write read

plot:
	$(SCRIPT) --function=$(FXN)
write:
	$(SCRIPT) --filename=$(TXT) 
read: 
	$(SCRIPT) --read_from_file=$(TXT) --print=$(FMT)  
