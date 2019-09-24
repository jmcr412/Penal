#python2
# coding=utf-8

apresentacao = "Bem-vindo ao programa de cálculo de penas para o crime de tráfico de droga.\nPor favor reporte erros e bugs para o e-mail joaomcrafael(at)protonmail.com"
print "\n\n\n",apresentacao,"\n"
pena = 5.0

#########################################################################################
# 1a Fase:
print "Responda às questões seguintes com ""s"" para sim ou ""n"" para não\n"

while True:
    criterio1_1 = raw_input("Critério 1 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_1 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_1 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_2 = raw_input("Critério 2 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_2 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_2 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_3 = raw_input("Critério 3 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_3 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_3 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_4 = raw_input("Critério 4 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_4 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_4 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_5 = raw_input("Critério 5 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_5 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_5 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_6 = raw_input("Critério 6 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_6 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_6 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_7 = raw_input("Critério 7 da 1a Fase: Aumentar a pena em 1/8?")
    if criterio1_7 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_7 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio1_8 = raw_input("Critério 8 da 1a Fase: Aumentar a pena em 1/8? Responder não baixará a pena em 1/6")
    if criterio1_8 == "s":
        pena = pena + (pena/8)
        break
    if criterio1_8 == "n":
        pena = pena - (pena/8)
        break
    else:
        print("Input incorrecto. Tente novamente")

    #limites da pena dentro da 1a Fase
if pena < 5:pena=5
if pena > 15:pena=15

#########################################################################################
# 2a Fase:

while True:
    criterio2_1 = raw_input("Critério 1 da 2a Fase: Aumentar a pena em 1/6?")
    if criterio2_1 == "s":
        pena = pena + (pena/6)
        break
    if criterio2_1 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

while True:
    criterio2_2 = raw_input("Critério 2 da 2a Fase: Diminuir a pena em 1/6?")
    if criterio2_2 == "s":
        pena = pena - (pena/6)
        break
    if criterio2_2 == "n":
        pass
        break
    else:
        print("Input incorrecto. Tente novamente")

#########################################################################################
#3a Fase

### INCOMPLETO

#########################################################################################
print "A condenação é de: %f anos" % (pena) #nao testado
