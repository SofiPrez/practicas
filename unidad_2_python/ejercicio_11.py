#!/usr/bin/python
sakura = raw_input ("ingrese sexo: ")
darien = int(input( "ingrese altura: "))
if darien <145 and sakura =="femenino":
	print "petiza"
elif 145<darien<170 and sakura =="femenino":
	print "normal"
elif darien>170 and sakura =="femenino":
	print "alta"
elif darien <160 and sakura =="masculino":
	print "petizo"
elif  160<darien<190 and sakura =="masculino":
	print "normal"
elif darien >190  and sakura =="masculino":
	print "alto"
else:
	print "alto jodido"
