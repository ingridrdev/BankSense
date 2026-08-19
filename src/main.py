print("=== BankSense ===")
print("Análise de risco de transações")
print("")

valor = float(input("Digite o valor da transação: R$ "))
hora = int(input("Digite a hora da transação (0 a 23): "))
tipo = input("Digite o tipo da transação (PIX, débito ou transferência): ")
novo_dispositivo = input("A transação foi feita em um novo dispositivo? (sim/não): ")
cidade_habitual = input("A transação foi feita em uma cidade habitual? (sim/não): ")

risco = 0

# Análise do valor
if valor > 3000:
    risco = risco + 40

# Análise do horário
if hora < 6:
    risco = risco + 30

# Análise do tipo de transação
if tipo.lower() == "pix":
    risco = risco + 10

# Análise do dispositivo
if novo_dispositivo.lower() == "sim":
    risco = risco + 10

# Análise da localização
if cidade_habitual.lower() == "não" or cidade_habitual.lower() == "nao":
    risco = risco + 10

# Define a classificação
if risco >= 60:
    classificacao = "ALTO RISCO"
elif risco >= 30:
    classificacao = "MÉDIO RISCO"
else:
    classificacao = "BAIXO RISCO"

# Formata o valor em reais
valor_formatado = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Relatório final
print("")
print("======================================")
print("       RELATÓRIO DA TRANSAÇÃO")
print("======================================")

print("Valor: R$", valor_formatado)
print(f"Horário: {hora:02d}:00")
print("Tipo:", tipo.upper())
print("Novo dispositivo:", novo_dispositivo.capitalize())
print("Cidade habitual:", cidade_habitual.capitalize())

print("")
print("----------- ALERTAS -----------")

if valor > 3000:
    print("- Valor acima do padrão")

if hora < 6:
    print("- Transação em horário incomum")

if tipo.lower() == "pix":
    print("- Transação realizada via PIX")

if novo_dispositivo.lower() == "sim":
    print("- Novo dispositivo detectado")

if cidade_habitual.lower() == "não" or cidade_habitual.lower() == "nao":
    print("- Localização fora do padrão")

print("")
print("--------------------------------------")
print("Score de risco:", risco, "/ 100")
print("Classificação:", classificacao)
print("======================================")