#-*- coding: utf-8 -*-

print ("")
print ("Nomenclaturas")
print ("------------------------------")
print ("")
print ("(V)(Volt) = Tensão")
print ("(I)(Ampere) = Corrente ")
print ("(R)(OHM) = Resistência ")
print ("(P)(Watt) = Potência ")
print ("")
print ("------------------------------")
print ("")
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Valor da potencisa (w): "))
tensao = float(input("Valor da tenção (v): "))
tempo = float(input("Tempo: "))
print ("")

ipv = potencia / tensao
consumoDiario = potencia * tempo
valorMensal = consumoDiario * 30
kwh = valorMensal / 1000

valor = 0.37 * kwh
print ("")
print("-----------------------")
print ("|",aparelho.upper())

print ("|","P = VI -> I = P / V =",int(potencia),"w","/",tensao,"v","=",round(ipv,2),"A")

print ("|","Consumo diario:",potencia,"w","*",tempo,"h","=",consumoDiario,"wh")

print ("|","Consumo mensal:","30dias","*",consumoDiario,"wh","=", valorMensal,"wh","/","1000","=",kwh, "kwh")

print ("|","Valor","0,37","*",kwh,"kwh","=","R$", valor)
print("-----------------------")
