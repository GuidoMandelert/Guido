#define posições

def define_posicoes(linha, coluna, orientacao ,tamanho):
    base=[0]*tamanho
    for i in range(int(tamanho)):   
        base[i]=[linha,coluna]
        if orientacao=='vertical':
            linha+=1
        if orientacao=='horizontal':
            coluna+=1
    return base

#preenche frota

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    nova_posicao=[]
    nova_posicao.append(define_posicoes (linha,coluna,orientacao,tamanho))
    if nome_navio not in frota: 
        frota[nome_navio]=nova_posicao
    else :
        posicao=frota[nome_navio]
        posicao.append(define_posicoes (linha,coluna,orientacao,tamanho))
        frota[nome_navio]=posicao
    return frota

#faz jogada

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

#posiciona frota

def posiciona_frota(frota):
    tabu=[[0]*10 for _ in range(10)]
    for barco in frota.values():
        for p in barco:
            for pos in p:
                x = pos[0]
                y = pos[1]
                tabu[x][y]=1
    return tabu

#Quantas embarcações afundadas?
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


