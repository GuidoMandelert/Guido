def posiciona_frota(frota):
    tabu=[[0]*10 for _ in range(10)]
    for barco in frota.values():
        for p in barco:
            for pos in p:
                x = pos[0]
                y = pos[1]
                tabu[x][y]=1
    return tabu