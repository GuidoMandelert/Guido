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
            for coord in frota:
                    if coord==i:
                        return False
    return True
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
frota={}
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
for i in quant:
    tipo=quant[i]
    tamanho=tam[i]
    print(f'Insira as informações referentes ao navio {i} que possui tamanho {tamanho} ')
    e=0
    while e<=(tipo-1):
        linha=int(input('linha: '))
        coluna=int(input('coluna: '))
        if i!="submarino":
            orientacao=int(input('orientação: '))
            if orientacao==1:
                orientacao='vertical'
            else:
                orientacao='horizontal'
        else:
            orientacao=1
        frota[i]=[linha,coluna]
        e+=1
        if posicao_valida(frota,linha,coluna,orientacao,tamanho)==False:
            print('Esta posição não está válida!')
            continue
        else:
            frota[i]=[preenche_frota(frota, tipo, linha, coluna, orientacao, tamanho)]
        e+=1
print(frota)