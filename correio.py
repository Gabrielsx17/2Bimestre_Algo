pacotes=("ABC123","XYZ789","DEF456","JKL321","MNO654","PQR987","STU741")

rastreio=["Enviado", "Recebido", "Em Trânsito" ,"Enviado", "Recebido","Em Trânsito","Enviado"]

i=0
codigos_do_Em_Transito=[]
quantidade_Enviado=rastreio.count("Enviado")
quantidade_Recibido=rastreio.count("Recebido")
quantidade_Em_Transito=rastreio.count("Em Trânsito")

for i in range (0, len("Em Trânsito")):
    if rastreio=="Em Trânsito":
        codigos_do_Em_Transito.append(pacotes[i])

pesquisa=input("Insira o código para verificar o status do pacote: ")
teste=pesquisa in pacotes
if teste==True:
    for i in range (0,len(pacotes)):
        if pesquisa==pacotes[i]:
            print(rastreio[i])
else:
    print("Este código não está na lista! ")

print("quantidade_Em_Transito: ",quantidade_Em_Transito)
print("quantidade_Enviado: ",quantidade_Enviado)
print("quantidade_Recibido :",quantidade_Recibido)
print("codigos_do_Em_Transito: ",codigos_do_Em_Transito)