def opFile(file):
	file = open(file, "r").read()
	return file
	
tokens = []

MATH = '+/%*'
DIGITS = '0123456789'
TT_DOT = "."

def lex(file):
	file = list(file)
        ###STRINGS###
	tok="" 
	string = ""
	expr=""
        wisk="" 
        ###INT###
	isexpr=1
        state=1
	wisks=1
     
	for char in file:
		tok+=char
		if tok=="\n":
			if expr!="" and isexpr==2:
				tokens.append("EXPR"+expr)
				expr=""
				tok=""
			elif expr!="" and isexpr==1:
				x = expr.count(".")
				if x >=1:
					tokens.append("FLOAT"+expr)
					expr=""
					tok=""
				else:
					tokens.append("INT"+expr)
					expr=""
					tok=""
			tok=""
		elif tok==" ":
		      tok=""
		elif tok=="print":
			tokens.append("PRINT")
			tok=""
		elif tok=="[" or tok=="(" or tok=="]" or tok==")":
		 	if wisks==1:
		 		wisks=2
		 	elif wisks==2:
		 		tokens.append("WISK"+wisk+tok)
		 		wisk=""
		 		wisks=1
		 		tok=""
		elif wisks==2:
		 	wisk+=tok
		 	tok=""
		elif tok=="END":
			tokens.append("END")
			tok=""
		elif tok in MATH and wisks==1:
			expr+=tok
			isexpr=2
			tok=""
		elif tok in DIGITS or tok in TT_DOT and state==1 and wisks==1:
		 	expr+=tok
		 	tok=""
		elif tok=="\"" or tok==" \"":
			if state==1:
				state=2
			elif state==2:
				tokens.append("STRING"+string+"\"")
				string=""
				state=1
				tok=""
		elif state==2:
			string+=tok
			tok=""
	print(tokens)
	return tokens

def puts(wisk, math):
	while wisk<=math:
		print(wisk)
		wisk+=1
	

def evalExpression(expr):
         #print(eval(expr))
         return eval(expr)

def parser(toks):
		i =0
		lina=0
		while(i<len(toks)):
			lina+=1
			if toks[i]+" "+toks[i+1][0:6]=="PRINT STRING" or toks[i]+" "+toks[i+1][0:6]=="PRINT NUM" :
				if toks[i+1][0:6]=="STRING":
					print(toks[i+1][7:-1])
				elif toks[i+1][0:3]=="NUM":
					print(toks[i+1][3:])
				i+=2
			elif toks[i]+" "+toks[i+1][0:4]=="PRINT EXPR":
				x = evalExpression(toks[i+1][4:])
				print(x)
				i+=2
			elif toks[i][0:4]=="WISK":
				x = toks[i][4:]
				print(x)
				a = 0
				b = 0
				if x.startswith("("):
					print("True")
					a+=1
				if x.endswith(")"):
					b+=1
				x= x[1:-1]
				x = list(x)
				tok=""
				WISK=[]
				for y in x:
					tok+=y
					if y==",":
						WISK.append(tok[:-1])
						tok=""
				WISK.append(tok)
				x= int(WISK[0])
				y=int(WISK[1])
				if a ==1 and b==1:
				   puts(x+a,y-b)
				elif a==1:
					puts(x+a,y)
				elif b==1:
					puts(x,y-b)
				else:
				   puts(x,y)
			    
				i+=1
				
				
			else:
				print(f"ERROR ON LINE {lina}")
				i+=1


		
	
def run():
	data = opFile("test.lang")
	toks = lex(data)
	parser(toks)

run()
