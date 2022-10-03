# O código é do @BrennoSullivan, só tô colocando aqui pra ficar mais fácil pro pessoal copiar.
import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []
for informacoes in json_data['cand']:

    if informacoes['seq'] in ('1', '2', '3', '4'):
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])

df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
    'Candidato', 'Nº de Votos', 'Porcentagem'
])

print(df_eleicao)

diferenca = round((float((porcentagem[0].replace(",", "."))) - 50), 3)

print("\nFaltam", diferenca, "% para o", candidato[0], "ganhar 🦑🇧🇷")