


#thuis opdracht 1 week 2 °°

# totaal_te_betalen=(f"{getal1*70.5 + getal2 * 20.89 + getal3 * 100.3}") 
# print(totaal_te_betalen)


getal1=int(input("hoeveel broeken werden er gekocht ?   >"))
getal2=int(input("hoeveel T-shirts werden er gekocht ?   >"))
getal3=int(input("hoeveel vesten werden er gekocht ?   >"))

def welkom_bij_de_cassa(getal1, getal2, getal3 ):
    som = getal1 * 70.5 + getal2 * 20.89 + getal3 * 100.3
    return som

totaal=welkom_bij_de_cassa(getal1 , getal2 , getal3)
print(f"{totaal}")

  
  #