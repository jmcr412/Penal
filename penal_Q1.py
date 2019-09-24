# 1a Fase sem loops para validacao de input
print "Responda as questoes seguintes com ""s"" para sim ou ""n"" para nao"


    criterio1_1 = raw_input("Criterio 1 da 1a Fase: Aumentar a pena em 1/8?");criterio1_2 = raw_input("Criterio 2 da 1a Fase: Aumentar a pena em 1/8?")
    criterio1_3 = raw_input("Criterio 3 da 1a Fase: Aumentar a pena em 1/8?");criterio1_4 = raw_input("Criterio 4 da 1a Fase: Aumentar a pena em 1/8?")
    criterio1_5 = raw_input("Criterio 5 da 1a Fase: Aumentar a pena em 1/8?");criterio1_6 = raw_input("Criterio 6 da 1a Fase: Aumentar a pena em 1/8?")
    criterio1_7 = raw_input("Criterio 7 da 1a Fase: Aumentar a pena em 1/8?");criterio1_8 = raw_input("Criterio 8 da 1a Fase: Aumentar ou diminuir a pena em 1/8?") #a 8 pode aumentar ou diminuir
    if criterio1_1 == "s":pena = pena + (pena/8)
    if criterio1_2 == "s":pena = pena + (pena/8)
    if criterio1_3 == "s":pena = pena + (pena/8)
    if criterio1_4 == "s":pena = pena + (pena/8)
    if criterio1_5 == "s":pena = pena + (pena/8)
    if criterio1_6 == "s":pena = pena + (pena/8)
    if criterio1_7 == "s":pena = pena + (pena/8)
    if criterio1_8 == "s":pena = pena + (pena/8)
    if criterio1_8 == "n":pena = pena - (pena/8)

#################################################################################################
	#1a fase - criterios de 1 a 7
criterio1=criterio2=criterio3=criterio4=criterio5=criterio6=criterio7=None
Primeira_Fase = [criterio1, criterio2, criterio3, criterio4, criterio5, criterio6, criterio7]
for criterio in Primeira_Fase:
	criterio = raw_input("Aumentar a pena em 1/8?")
	if criterio == "s":
        pena = pena + (pena/8)
	if criterio == "n":
		pass
	else:
		print("Input incorrecto. Tente novamente")

##################################################################################################
#1a fase com loops para validacao de input
while True:
    criterio1_1 = raw_input("Criterio 1 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_1 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_1 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_2 = raw_input("Criterio 2 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_2 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_2 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_3 = raw_input("Criterio 3 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_3 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_3 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_4 = raw_input("Criterio 4 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_4 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_4 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_5 = raw_input("Criterio 5 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_5 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_5 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_6 = raw_input("Criterio 6 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_6 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_6 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_7 = raw_input("Criterio 7 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_7 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_7 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_8 = raw_input("Criterio 8 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_8 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_8 == "n":
        pena = pena - (pena/8)
        break
    else:
        print("Input incorrecto. Tente novamente")
