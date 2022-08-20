import datetime


def suma(event: dict[str, int]) -> dict:
    """
    Funcion que toma dos operandos y devuelve la suma.
    :param event: payload JSON with parameters from AWS test.
    :return: diccionario con la suma de los operandos.
    """
    print(type(event))
    operando_a = event['operando_a']
    operando_b = event['operando_b']
    if not isinstance(operando_a, int) or not isinstance(operando_b, int):
        raise Exception('Parametros no son numeros enteros')
    return {
        "status": 200,
        "message": "ok",
        "suma": operando_b + operando_a
    }


def fecha_actual() -> dict:
    """
    Function que calculal la hora actual del servidor.
    :return: diccionario con la hora.
    """
    return {
        "status": 200,
        "message": "ok",
        "suma": datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%s')
    }

