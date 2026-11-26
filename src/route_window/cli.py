"""Print a JSON summary for a route given on the command line."""

import argparse
import json

from .overview import summarize
from .stops import loops, path_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stops", nargs="+", help="Ordered stop codes, e.g. A B A")
    args = parser.parse_args()
    report = summarize(args.stops)
    report.update(path_count=path_count(args.stops), loops=loops(args.stops))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
