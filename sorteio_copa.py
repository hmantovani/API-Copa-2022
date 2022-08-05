import pandas as pd

class copamundo():
    def sorteio_copa(self):
        df = pd.read_csv('API_copa2022\potes_copa22.csv')
        df.sort_values('POTE', inplace=True) # Garantir que os times estejam listados em ordem do pote 1 ao 4
        num_times = 31
        grupoA = ['Qatar']
        grupoB = []
        grupoC = []
        grupoD = []
        grupoE = []
        grupoF = []
        grupoG = []
        grupoH = []
        grupos = [grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH]

        # Quantidade de times por pote
        qp1 = (df['POTE'].values == 1).sum()
        qp2 = (df['POTE'].values == 2).sum()
        qp3 = (df['POTE'].values == 3).sum()
        qp4 = (df['POTE'].values == 4).sum()

        # Criação de listas para cada pote
        times = df['PAÍS'].tolist()
        pote1 = times[0:qp1]
        pote2 = times[qp1:qp1+qp2]
        pote3 = times[qp1+qp2:qp1+qp2+qp3]
        pote4 = times[qp1+qp2+qp3:num_times]

        # Sorteio do pote 1
        import random
        random.shuffle(pote1)
        grupoB.append(pote1[0])
        grupoC.append(pote1[1])
        grupoD.append(pote1[2])
        grupoE.append(pote1[3])
        grupoF.append(pote1[4])
        grupoG.append(pote1[5])
        grupoH.append(pote1[6])

        # Sprteio do pote 2
        random.shuffle(pote2)
        grupoA.append(pote2[0])
        grupoB.append(pote2[1])
        grupoC.append(pote2[2])
        grupoD.append(pote2[3])
        grupoE.append(pote2[4])
        grupoF.append(pote2[5])
        grupoG.append(pote2[6])
        grupoH.append(pote2[7])

        # Sprteio do pote 3
        random.shuffle(pote3)
        grupoA.append(pote3[0])
        grupoB.append(pote3[1])
        grupoC.append(pote3[2])
        grupoD.append(pote3[3])
        grupoE.append(pote3[4])
        grupoF.append(pote3[5])
        grupoG.append(pote3[6])
        grupoH.append(pote3[7])

        # Sprteio do pote 4
        random.shuffle(pote4)
        grupoA.append(pote4[0])
        grupoB.append(pote4[1])
        grupoC.append(pote4[2])
        grupoD.append(pote4[3])
        grupoE.append(pote4[4])
        grupoF.append(pote4[5])
        grupoG.append(pote4[6])
        grupoH.append(pote4[7])

        copa22 = ['Grupo A', grupoA,
                'Grupo B', grupoB,
                'Grupo C', grupoC,
                'Grupo D', grupoD,
                'Grupo E', grupoE,
                'Grupo F', grupoF,
                'Grupo G', grupoG,
                'Grupo H', grupoH]

        return(copa22)