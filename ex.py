features = [
    "depositar", "sacar", "transferir", "investir", "resgatar", "converter", "bloquear", "desbloquear", "extratar", "auditar",
]

def gerar_subconjuntos(features):
    if not features:
        return [()]
    
    primeiro = features[0]
    resto = gerar_subconjuntos(features[1:])
    
    casos = []

    for subconjunto in resto:
        casos.append(((primeiro, False),) + subconjunto)
        casos.append(((primeiro, True),) + subconjunto)
    return casos

todas = gerar_subconjuntos(features)
print(f"\n -- Número total de combinações: {len(todas)} --")
print("\nExemplos de combinações:")
for caso in todas[:5]:
    print(caso)