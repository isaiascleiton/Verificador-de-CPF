print("="*30)
print("VERIFICADOR DE CPF")
print("="*30)

print("\033[31mEX : 111.222.333-44\033[m")
print("\033[31mOBS: Digite com os '.' e '-' \033[m")
cpf = str(input("Digite o cpf que deseja ser analisado: ")).strip()
n1 = int(cpf[0])
n2 = int(cpf[1])
n3 = int(cpf[2])
n4 = int(cpf[4])
n5 = int(cpf[5])
n6 = int(cpf[6])
n7 = int(cpf[8])
n8 = int(cpf[9])
n9 = int(cpf[10])

v1 = (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)
if (v1 % 11) < 2 :
    v1 = 0
else :
    v1 = 11 - (v1 % 11)

v2 = (n1 * 11)+(n2 * 10)+(n3 * 9)+(n4 * 8)+(n5 * 7)+(n6 * 6)+(n7 * 5)+(n8 * 4)+(n9 * 3)+(v1 * 2)
if (v2 % 11) < 2 :
    v2 = 0
else :
    v2 = 11 - (v2 % 11)  

sv1 = str(v1)
sv2 = str(v2)

confere = ( cpf[0] + cpf[1] + cpf[2] + '.' + cpf[4] + cpf[5] + cpf[6] + '.' + cpf[8] + cpf[9] + cpf[10] + '-' + sv1  + sv2 ) 

if confere == cpf :
    print("o CPF {} é \033[42mVÁLIDO\033[m.".format(cpf))
else :
    print("O CPF {} é \033[41mINVÁLIDO\033[m.".format(cpf))
