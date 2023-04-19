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
    base=grid[linha][coluna]
    posicao=[]
    if orientacao=='vertical':
        for i in range(tamanho):
            posicao.append(grid[linha+i],[coluna])
    if orientacao=='horizontal':
        for i in range(tamanho):
            posicao.append(grid[linha],[coluna+i])
    return posicao
print (define_posicoes(2, 3,'vertical' ,4))