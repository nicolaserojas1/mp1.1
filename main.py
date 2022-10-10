# Parte 1: Cargar los datos

import readline


def cargar_datos(ruta_archivo:str):
    #lee archivo
    f = open(ruta_archivo,"r",encoding="utf-8")
    lineas = f.readlines()
    f.close()

    #Estrucutras solicitasdas
    tipos_pokemon = list()
    pokemon_por_tipo = dict()
    info_pokemon = dict()
    
    #ciclo generador tipos_pokemon

    for linea in lineas:
        separadas = linea.split(",")
        id_pokemon = separadas[0]
        nombre = separadas[1] 
        tipos= separadas[2]
        hp = separadas[3]
        ataque = separadas[4]
        defensa = separadas[5]
        generacion = separadas[6]
        
        for item in separadas:
            if item == tipos:
                tipos_pokemon.append(item)
            else:
                pass
     
    
    #ciclo generador pokemon_por_tipo
    for linea in lineas:
        id_pokemon,nombre,tipo,hp,ataque,defensa,generacion = linea.split(",")
        if id_pokemon == "id":
            pass
        else:
            if tipo not in pokemon_por_tipo.keys():
                pokemon_por_tipo[tipo] = [id_pokemon]
            else:

                pokemon_por_tipo[tipo].append(id_pokemon)

    return pokemon_por_tipo, set(tipos_pokemon)

    #ciclo generador info_pokemon

    f = open(ruta_archivo, "r", encoding="utf-8")
    lineas = f.readlines()
    f.close()

    for linea in lineas:
        columnas = linea.split(",")
        id_pokemon = columnas[0]
        columnas[6] = columnas[6].strip()
        atributos = columnas[1:]


        sub_info_poquemon = dict()
        if atributos[0] == "nombre":
            pass
        else:         
            sub_info_poquemon["nombre"] = atributos[0]
            sub_info_poquemon["tipo"] = atributos[1]
            sub_info_poquemon["hp"] = atributos[2]
            sub_info_poquemon["ataque"] = atributos[3]
            sub_info_poquemon["defensa"] = atributos[4]
            sub_info_poquemon["generacion"] = atributos[5]
            if id_pokemon not in info_pokemon:
                info_pokemon[id_pokemon] = sub_info_poquemon
            else:
                break
    return info_pokemon
    

# Parte 2: Completar las consultas

def obtener_ataque_y_defensa(nombre_pokemon):
    # Completar
    pass

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
