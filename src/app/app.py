import argparse
from ._version import __version__
from .pareto_front_generator import ParetoFrontGenerator
from .file_view import FileView
from .loader import Loader 
from .monotic_decreasing_functions import monotic_decreasing_function_factory, search_monotic_decreasing_function_subclasses, Polynomial
import time

def main(parser=argparse.ArgumentParser(prog="gen-set", description="Non-dominated set generator")):
    parser.add_argument(
        "-v", "--version", action="store_true", help="shows the app version."
    )
    parser.add_argument(
        "-dim", "--dimension", type=int, required=False, help="it's the non-dominated set dimension", default=2
    )
    parser.add_argument(
        "-p", "--points", type=int, required=False, help="It generates number of points", default=50
    )
    parser.add_argument(
        "-m", "--function", 
        type=monotic_decreasing_function_factory, 
        required=False, 
        help="It applies monotic decreasing function R^n -> R such that Df<0 in (R^n)+ in order to generate non-dominated space", 
        default=Polynomial,
        choices=search_monotic_decreasing_function_subclasses()
    )
    parser.add_argument(
        "-t", "--translation", type=float, nargs='*', help="It translates generated space", default=[0]
    )
    parser.add_argument(
            "-f", "--file", required=False, help="It writes a file given a file's name", default=str(time.ctime()).replace(" ", "_")+".pof"
    )
    args = parser.parse_args()

    if args.version:
        return __version__
    with Loader("Generating non-dominated set (aka pareto front)..."):
        pareto_front_generator = ParetoFrontGenerator(dim=args.dimension, points=args.points, translation=args.translation, function=args.function)
        pareto_front = pareto_front_generator.generate_space()
        fileView = FileView(args.file, pareto_front)
        fileView.make()
