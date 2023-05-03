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
    if dic=={}:
        return False
    barco=define_posicoes(lin,col,orientacao,tamanho)
    for i in barco:
        a=i[0]
        b=i[1]
        if a>9 or b>9:
            return False
print(posicao_valida({
    'navio-tanque': [[[4, 9], [5, 9], [6, 9]], [[6, 3], [7, 3], [8, 3]]],
    "contratorpedeiro":[
      [[4,3],[4,4]]],
    "submarino": [
      [[0,0]],
      [[0,1]],
      [[0,2]],
      [[0,3]]
    ],
},2,9,'horizontal',2))