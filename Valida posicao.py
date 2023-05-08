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