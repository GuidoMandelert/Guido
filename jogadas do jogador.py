def afundados(frota,tabu):
  resp=0
  for barco in frota:
    barco=frota[barco]
    for unidade in barco:
      resp+=1
      for local in unidade:
        x=local[0]
        y=local[1]
        if tabu[x][y]!='X':
          resp-=1
          break
  return resp
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro
def posiciona_frota(frota):
    tabu=[[0]*10 for _ in range(10)]
    for barco in frota.values():
        for p in barco:
            for pos in p:
                x = pos[0]
                y = pos[1]
                tabu[x][y]=1
    return tabu
def define_posicoes(linha, coluna, orientacao ,tamanho):
    base=[0]*tamanho
    for i in range(int(tamanho)):   
        base[i]=[linha,coluna]
        if orientacao=='vertical':
            linha+=1
        if orientacao=='horizontal':
            coluna+=1
    return base
def posicao_valida(dic,lin,col,orientacao,tamanho):
    barco=define_posicoes(lin,col,orientacao,tamanho)
    for i in barco:
        if i[0]>9 or i[1]>9:
            return False
        for e in dic:
            frota=dic[e]
            for boat in frota:
                for coord in boat:
                    if coord==i:
                        return False
    return True
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    nova_posicao=[]
    nova_posicao.append(define_posicoes (linha,coluna,orientacao,tamanho))
    barco=frota[nome_navio]
    if barco==[]: 
        frota[nome_navio]=nova_posicao
    else :
        posicao=barco
        posicao.append(define_posicoes (linha,coluna,orientacao,tamanho))
        frota[nome_navio]=posicao
    return frota
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
quant = {
    "porta-aviões":1,
    "navio-tanque":2,
    "contratorpedeiro":3,
    "submarino": 4,
}
tam = {
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1,
}
for i in frota.keys():
    e=0
    tamanho=tam[i]
    while e<quant[i]:
        print(f'Insira as informações referentes ao navio {i} que possui tamanho {tamanho}')
        linha=int(input('linha: '))
        coluna=int(input('coluna: '))
        if i!="submarino":
            orientacao=int(input('orientação: '))
            if orientacao==1:
                orientacao='vertical'
            else:
                orientacao='horizontal'
        if posicao_valida(frota,linha,coluna,orientacao,tamanho)==False:
            print('Esta posição não está válida!')
        else:
            frota_jogador=preenche_frota(frota, i, linha, coluna, orientacao, tamanho)
            e+=1
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

jogando=True
jogadas=[]
tabuleiro_oponente=posiciona_frota(frota_oponente)
tabuleiro_jogador=posiciona_frota(frota_jogador)
while jogando==True:
    
    mapa=monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(mapa)
    while True:
        while True:
            linha=int(input('linha: '))
            if linha<0 or linha>9:
                print('Linha inválida!')
            else:
                break
        while True:
            coluna=int(input('coluna: '))
            if coluna<0 or coluna>9:
                print('coluna inválida!')
            else:
                break
        if [linha,coluna] in jogadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            break 
    jogadas.append([linha,coluna])
    tabuleiro_oponente=faz_jogada(tabuleiro_oponente,linha,coluna)
    monitoria=afundados(frota_oponente,tabuleiro_oponente)
    if monitoria==10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break