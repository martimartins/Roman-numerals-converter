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

def ConvertNumberRoman(value: int) -> str:
    """
    Função para converter numero inteiros para numeros romanos usando dict(numeros_rumanos),
    ele verifica cada item da dict e vê se o valor do item é menor que o number_remening(value),
    se sim ele adiciona a str roman_number e diminui pelo valor do item.
    """
    roman_number = ""
    number_remening = int(value)
    count = 0
    # VER TODO O DICIONARIO numeros_rumanos
    for num in list(numeros_rumanos):
        # VERIFICA SE O VALOR DO ITEM É MENOR OU IGUAL AO NUMBER_REMENING(VALUE)
        while int(numeros_rumanos[num]) <= int(number_remening):
            # ADICIONAR O VALOR DO ITEM (Exemple: X;V;I) A STR roman_number
            if num == "M":
                count += 1
            roman_number += num
            # DIMINUIR AO VALOR TOTAL DO NUMERO PEDIDO EM ROMAN
            number_remening -= int(numeros_rumanos[num])
    # RETURNAR O VALOR FINAL (o valor romano)
    if count > 1:
        roman_number = roman_number.replace("M"*count, "M*"+str(count)+" ")
    return str(roman_number)


def ConverterRomanNumber(value: str) -> str:
    """
    Função para converter numeros rumanos em numeros inteiros usando dict(numeros_rumanos),
    ele vericia cada item na dict, e verifica se existe no value(valor inserido pelo usuario).
    """
    total_number = 0
    index_position = 0
    # VER TODO O DICIONARIO numeros_rumanos
    for num in list(numeros_rumanos):
        # VERIFICAR SE O item DO DICIONARIO TEM NO VALUE(input)
        while str(num) == value[index_position:index_position+len(num)]:
            # ADICIONAR PELO DICIONARIO O VALOR DA LETRA ROMANA (Exemple: X: 10)
            total_number += numeros_rumanos[num]
            # ADICIONAR O NUMERO DE CARACTERES QUE O NUMERO ROMANO TINHA, PARA O WHILE NÃO VERIFICAR SEMPRE A MESMA LETRA
            index_position += len(num)
    # RETURNAR O VALOR FINAL
    return str(total_number)

def main() -> None:
    print("Convertor de numeros rumanos\n\n")

    value = input(">> ")
    try:
        int(value)
        print("\n/*= "+ConvertNumberRoman(value))
    except:
        print("\n/*= "+ConverterRomanNumber(value))
try:
    main()
except KeyboardInterrupt:
    print("\rAdeus!")
