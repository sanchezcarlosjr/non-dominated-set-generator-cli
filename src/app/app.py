import argparse
from ._version import __version__
from .pareto_front_generator import ParetoFrontGenerator
from .file_view import FileView
import time

def main(parser=argparse.ArgumentParser(prog="gen-set", description="Non-dominated set generator")):
    parser.add_argument(
        "-v", "--version", action="store_true", help="shows the app version."
    )
    parser.add_argument(
        "-dim", "--dimension", type=int, required=False, help="it's the non-dominated set dimension", default=2
    )
    parser.add_argument(
        "-p", "--points", type=int, required=False, help="generate number of points", default=50
    )
    parser.add_argument(
        "-t", "--translation", type=int, nargs='*', help="apply translation to generated space", default=[0]
    )
    parser.add_argument(
            "-f", "--file", required=False, help="file's name", default=str(time.ctime()).replace(" ", "_")+".pof"
    )
    args = parser.parse_args()

    if args.version:
        return __version__
    pareto_front_generator = ParetoFrontGenerator(dim=args.dimension, points=args.points, translation=args.translation)
    pareto_front = pareto_front_generator.generate_space()
    fileView = FileView(args.file, pareto_front)
    fileView.make()
