from .converter import *
convert_measure(1000, 'mm', 'm')      # → 1.0
convert_measure(1.5, 'kg', 'g')       # → 1500.0
convert_measure(0, 'c', 'f')          # → 32.0
convert_measure(-273.15, 'c', 'k')    # → ~0.0
convert_measure(-300, 'c', 'k')       # → BelowAbsoluteZeroError
convert_measure(1, 'kg', 'm')         # → IncompatibleUnitsError
convert_measure(100, 'CM', 'm')       # → 1.0 (регистр)