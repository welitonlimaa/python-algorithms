# Python Algorithms
Este é um repositório contendo soluções para vários desafios de algoritmos implementados em Python. Cada desafio representa um problema específico que requer habilidades de resolução de problemas e otimização de algoritmos.

Os desafios incluem:

1. **Número de estudantes estudando no mesmo horário (Algoritmo de busca)**: Encontrar o melhor horário para disponibilizar conteúdo de estudo com base nos dados de entrada.
> solução em challenge_study_schedule.py
2. **Criptografia de inversões (Testes)**: Implementar testes para uma função de criptografia.
> solução em challenge_encrypt_message.py
3. **Palíndromos (Recursividade)**: Verificar se uma palavra é um palíndromo usando uma solução recursiva.
> solução em challenge_palindromes_recursive.py
4. **Anagramas (Algoritmo de ordenação)**: Comparar duas strings, ordená-las e identificar se são anagramas.
> solução em challenge_anagrams.py
5. **Encontrando números repetidos (Algoritmo de busca)**: Encontrar um número duplicado em uma lista de números inteiros.
> solução em challenge_find_the_duplicate.py
6. **Palíndromos (Iteratividade)**: Verificar se uma palavra é um palíndromo usando uma solução iterativa.
> solução em challenge_palindromes_iterative.py

## Como utilizar

Clone o repositório:
```bash
git clone https://github.com/welitonlimaa/python-algorithms.git
```

Crie o ambiente virtual para o projeto
```bash
python3 -m venv .venv && source .venv/bin/activate
```

Instale as dependências
```bash
python3 -m pip install -r dev-requirements.txt
```

Navegue até o diretório do desafio desejado, por exemplo:
```bash
cd python-algorithms/challenges/challenge_study_schedule
```

Execute os testes para verificar se a solução está correta:
```bash
pytest
```

