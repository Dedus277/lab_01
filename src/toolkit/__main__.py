import argparse
import sys

from .calculator import calculate
from .converter import convert_measure
from .errors import ToolkitError


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Калькулятор и конвертер величин",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    calc = sub.add_parser("calc", help="Вычислить арифметическое выражение")
    calc.add_argument("expression", help='Выражение, например "2+3*4"')

    conv = sub.add_parser("convert", help="Конвертировать величину")
    conv.add_argument("value", type=float, help="Числовое значение")
    conv.add_argument("--from", dest="from_unit", required=True, help="Исходная единица")
    conv.add_argument("--to", dest="to_unit", required=True, help="Целевая единица")

    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "calc":
        result = calculate(args.expression)
    else:
        result = convert_measure(args.value, args.from_unit, args.to_unit)

    print(result)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ToolkitError as e:
        print(e, file=sys.stderr)
        sys.exit(2)