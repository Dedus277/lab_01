measures = {
    'mm': 0.001,
    'cm': 0.01,
    'm', 1,
    'dm': 0.1,
    'km': 1000,
    'kg': 1,
    'g': 0.001
}
def convert_len(value,from_measure,to_measure):
    return value * measures(from_measures) / measures(to_measures)
