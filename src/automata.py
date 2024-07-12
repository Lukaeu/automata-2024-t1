def load_automata(filename):

   ```
    a b
    q0 q1 q2 q3
    q0 q3
    q0
    q0 a q1
    q0 b q2
    q1 a q0
    q1 b q3
    q2 a q3
    q2 b q0
    q3 a q1
    q3 b q2
    ```
    if isinstance(filename, str):
        if not filename.endswith('.txt'):
            filename += '.txt'
        resposta = {}
    else:
        raise Exception('O tipo esperado para o nome do arquivo é string')
        
    try:
        with open(filename, "rt") as arquivo:
            linhas, regras = arquivo.readlines(), []
            resposta['simbolos'] = linhas[0].strip().split(' ')
            resposta['estados'] = linhas[1].strip().split(' ')
            possiveis_estados_finais, estados_finais = linhas[2].strip().split(' '), []
            for estado in possiveis_estados_finais:
                if estado in resposta['estados']:
                    estados_finais.append(estado)
                else:
 
