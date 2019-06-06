import re
a = "Rua Marechal Floriano, 405 - segundo andar. CEP 96810-002"
b = "Rua 7 de setembro, 59, apto 302, CEP 96810-016"
c = "Rua Vinte e Oito de Setembro, 1997, CEP 96814-200"
rua = re.search("(^R..\s*[\w a-z]*,)",c)
casa = re.search("(([,]\s*[0-9]*[,](\s*[a-z 0-9]*))|([,]\s*[0-9]*\s[-|,]\s*[a-z A-Z]*[,|\.]))",c)
cep = re.search("(\s[A-Z]{3}\s\d{5}[-]\d{3})",c)
print(rua)
print(casa)
print(cep)
#(^R..\s*[\w a-z]*,)
#(([,]\s*[0-9]*[,](\s*[a-z 0-9]*))|([,]\s*[0-9]*\s[-|,]\s*[a-z A-Z]*[,|\.]))
#(\s[A-Z]{3}\s\d{5}[-]\d{3})

#(([,]\s*[0-9]*[,])|([,]\s*[0-9]*\s[-|,]\s*[a-z A-Z]*[,|\.]))
