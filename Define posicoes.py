def define_posicoes(linha, coluna, orientacao ,tamanho):
    tam=int(tamanho)
    base=[0]*tamanho
    for i in range(tam):   
        if orientacao=='vertical':
            base[i]=[linha,coluna]
            linha+=1
        if orientacao=='horizontal':
            base[i]=[linha,coluna]
            coluna+=1
    return base