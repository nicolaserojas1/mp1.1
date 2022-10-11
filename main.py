from collections import deque
from typing import DefaultDict, DefaultDict

# Parte 1: Cargar los datos
def cargar_datos(ruta_archivo:str)->tuple:

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        no_duplicados = list()
        for linea in f:    
            id_pokemon,nombre,tipo,hp,ataque,defensa,generacion = linea.strip().split(",")
            if id_pokemon not in no_duplicados:
                no_duplicados.append(linea)
            else:
                pass
        lista_final = list()
        for item in no_duplicados:
            serparados = item.strip().split(",")
            lista_final.append(serparados)

    # lista de tipos_pokemon
    tipos_pokemon = list()
    for elemento in lista_final:
        tipoPokemon = elemento[2]
        if tipoPokemon not in lista_final:
            tipos_pokemon.append(tipoPokemon)
        else:
            pass
    tipos_pokemon = set(tipos_pokemon)
    tipos_pokemon = list(tipos_pokemon)

    # diccionario pokemon_por_tipo
    pokemon_por_tipo =dict()
    for tipo in tipos_pokemon:
        lista_id = list()
        for elemento in lista_final:
            pokemon_por_tipo[tipo] = lista_id
            if tipo == elemento[2]:
                lista_id.append(elemento[0])
            else:
                pass

    # # diccionario pokemon_por_tipo info_pokemon
    info_pokemon = dict()
    info_pokemon_atributos = dict()
    for elemento in lista_final:

        info_pokemon_atributos["nombre"] = elemento[1]
        info_pokemon_atributos["tipo"] = elemento[2]
        info_pokemon_atributos["hp"] = elemento[3]
        info_pokemon_atributos["ataque"] = elemento[4]
        info_pokemon_atributos["defensa"] = elemento[5]
        info_pokemon_atributos["generacion"] = elemento[6]
        if elemento[0] == "id":
            pass
        else:
            if elemento[0] not in info_pokemon.values():
                info_pokemon[elemento[0]] = info_pokemon_atributos
            else:
                info_pokemon[elemento[0]].update(info_pokemon_atributos)
    return info_pokemon, tipos_pokemon

# Parte 2: Completar las consultas

def obtener_ataque_y_defensa(nombre_pokemon)->tuple:
    for k, v in info_pokemon.items():
        for k2, v2 in v.items():
            if v2 == nombre_pokemon:
                resultado = v["ataque"], v["defensa"]
                resultado = tuple(resultado)
    return(resultado)

def filtrar_y_ordenar(tipo_pokemon, criterio):
    # Completar
    pass

def obtener_estadisticas(tipo_pokemon, criterio):
    # Completar
    pass


def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener ataque y defensa de un pokemon")
    print("[2] Filtrar y ordenar pokemons")
    print("[3] Obtener estadísticas de pokemons")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def revisar_estructuras(tipos_pokemon, pokemon_por_tipo, info_pokemon):
    print("\nTipos de pokemon:")
    for tipo in tipos_pokemon:
        print(f"    - {tipo}")

    print("\nId de pokemons por tipo:")
    for tipo in pokemon_por_tipo:
        print(f"    Tipo: {tipo}")
        for id_ in pokemon_por_tipo[tipo]:
            print(f"        - {id_}")

    print("\nInformación de cada pokemon:")
    for id_ in info_pokemon:
        print(f"    Id: {id_}")
        for llave in info_pokemon[id_]:
            print(f"        - {llave}: {info_pokemon[id_][llave]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre del pokemon: ")
    return nombre


def solicitar_tipo_y_criterio():
    tipo = input("\nIndique el tipo de pokemon: ")
    criterio = input("\nIndique el criterio (hp, ataque, defensa): ")
    return tipo, criterio


def main():
    datos_cargados = True
    try:
        tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()
    except TypeError as error:
        if 'cannot unpack non-iterable NoneType object' in repr(error):
            print("\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n")
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(tipos_pokemon, pokemon_por_tipo, info_pokemon)

            elif accion == 1:
                nombre_pokemon = solicitar_nombre()
                ataque, defensa = obtener_ataque_y_defensa(nombre_pokemon)
                print(f"\nObteniendo ataque y defensa de {nombre_pokemon}")
                print(f"    - Ataque: {ataque}")
                print(f"    - Defensa: {defensa}")

            elif accion == 2:
                tipo, criterio = solicitar_tipo_y_criterio()
                nombres_pokemon = filtrar_y_ordenar(tipo, criterio)
                print(f"\nNombres de pokemon tipo {tipo} ordenados segun {criterio}:")
                for nombre in nombres_pokemon:
                    print(f"    - {nombre}")

            elif accion == 3:
                tipo, criterio = solicitar_tipo_y_criterio()
                estadisticas = obtener_estadisticas(tipo, criterio)
                print(f"\nEstadísticas de {criterio} de pokemon tipo {tipo}:")
                print(f"    - Máximo: {estadisticas['max']}")
                print(f"    - Mínimo: {estadisticas['min']}")
                print(f"    - Promedio: {estadisticas['prom']}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
