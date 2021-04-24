# Roman numerals converter

Converter números romanos em números e converter números em numerais romanos.

## Como funciona
Dicionário usado na script | este dicionário inclui todas as regras dos números romanos, mesmo os subtraídos,
se o valor for invalido como por exemplo (VX) ele apenas vai contar o valor primeiro valor valido que encontrar na dict(numeros_rumanos).

    numeros_rumanos = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L" : 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
    }

Script usa uma dicionário com todas as letras romanas necessárias (incluindo os casos que são subtraídos), no total são 13 itens na dict,

index_position é uma variável que existe na função  para converter números romanos em números para prevenir que o while não execute sempre para a mesma caracter, se o while encontrar alguma caracter no value que esteja também no dict ele vai somar a variavel index_position a quantidade de caracteres que o item tinha usando len().

para converter números romanos em números ele vê cada item no list(dict), e while para executar se o item da dict tiver no value(input do utilizador)[index_position:index_position+len(num)] (ou seja do value ele apenas pega o valor que estiver no dicionário e se estiver ele vai somando a quantidade de caracteres que o item têm index_position), se sim ele soma o valor do item ao resultado final e assim ele vai somando de acordo com as regras e o alfabeto dos números romanos.

para converter números para números romanos, ele vê cada item no dict e while para executar se tiver um item da dict no value(input do utilizador) ele vai somar o item a variável roman_number(str) que ira ser retornada quando a função acabar.

## Executar

Esta script apenas foi testada com [python3](https://www.python.org/downloads/release/python-389/), para executar a script use.

### Windows
    py main.py
### Linux
    py main.py

### Baixe python
[Windows](https://www.python.org/downloads/release/python-389/)
Linux -> `sudo apt-get install python3`

![Scirpt preview](https://i.imgur.com/0aidoe7.png)