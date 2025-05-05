
def calculadora_imc(pessoa):
    imc = pessoa["peso"]/(pessoa["altura"]*pessoa["altura"])
    resultado = (f"O IMC {pessoa["nome"]} é {imc:.2f}")
    saudavel = 18.5 <imc < 25

    return{
        "nome": pessoa["nome"],
        "imc": round(imc,2),
        "resultado": resultado,
        "saudavel": saudavel,
    }

pessoa1={
    "nome": "José",
    "peso": 110,
    "altura": 1.75
}

pessoa2={
    "nome": input("Digite o nome da segunda pessoa:\n"),
    "peso": int(input("Digite o peso da segunda pessoa:\n")),
    "altura": float(input("Digite a altura da segunda pessoa em metros:\n"))
}

print(calculadora_imc(pessoa1))
print(calculadora_imc(pessoa2))