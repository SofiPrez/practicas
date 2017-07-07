#!/usr/bin/python
akira =int(input ("ingrese nro de pasajeros: "))
if akira ==0: 
	print "no hay transporte"
elif akira==1 and akira< 2:
	print "su transporte es bicicleta"
elif akira==2 or akira<3: 
	print  "su transporte es moto"
elif akira==3 or  akira<5: 
	print "su transporte es auto"
elif  akira==5 or akira<13:
	print "su transporte es camioneta"
elif akira==13 or akira<41:
	print "su transpote es colectivo"
elif akira==41 or akira<201:
	print "su transporte es avion"
else : 
	print "su transporte es nave espacial"
