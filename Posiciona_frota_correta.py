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
            frota=preenche_frota(frota, i, linha, coluna, orientacao, tamanho)
            e+=1
print(frota)