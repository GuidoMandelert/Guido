def define_posicoes(linha, coluna, orientacao ,tamanho):
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    tam=int(tamanho)
    base=[0]*tamanho
    for i in range(tam):   
        if orientacao=='vertical':
            base[i]=[linha,coluna]
            linha+=1
        if orientacao=='horizontal':
            base[i]=[linha,coluna]
            col+=1
    return base
print (define_posicoes(2, 3,'vertical' ,4))