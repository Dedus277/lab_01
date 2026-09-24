length = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'dm': 0.1,
    'km': 1000.0,
}
mass = {
    'kg': 1,
    'g': 0.001
}
abs_zero = {
    "C": -273.15,
    "K": 0.0,
    "F": -459.67
}
def group(unit:str):
    if unit in length:
        return 'length'
    if unit in mass:
        return "mass"
    if unit in abs_zero:
        return "degree"
    return None
def convert_measure(value: float,from_measure: str,to_measure:str):
    from_measure = from_measure.lower()
    to_measure = to_measure.lower()

    group_from = group(from_measure)
    group_to = group(to_measure)
    if group_from is None or group_to is None:
        raise UnknownUnitError(f"{from_measure} и {}")
    if group_from != group_to:
        raise IncompatibleUnitsError(f"{from_measure} и {to_measure} несовместимы")
    if group_from == 'degree':
        if value < abs_zero[from_measure]:
            raise IncompatiblUnitsError("Ниже абсолютного нуля")
        return convert_temprature(value,from_measure, to_measure)
    table = length if group_from == 'length' else mass
    return float(value*table[from_measure]/table[to_measure])
    