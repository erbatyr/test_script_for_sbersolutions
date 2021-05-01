import sys

import pandas as pd
import argparse


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="merging to jsonl files data")
    parser.add_argument(
        'path_to_log1',
        metavar='<PATH TO LOG1>',
        type=str,
        help='path to log1 jsonl file',
    )

    parser.add_argument(
        'path_to_log2',
        metavar='<PATH TO LOG2>',
        type=str,
        help='path to log2 jsonl file',
    )

    parser.add_argument(
        'path_to_merged_log',
        metavar='<PATH TO RESULT LOG>',
        type=str,
        help='path to merged jsonl file',
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    sys.stdout.write("\rgetting log1...")
    a = pd.read_json(args.path_to_log1, lines=True)

    sys.stdout.write("\rgetting log2...")
    b = pd.read_json(args.path_to_log2, lines=True)

    sys.stdout.write("\rconcatenate 2 logs...")
    result = pd.concat([a, b])

    sys.stdout.write("\rgrouping by timestamp...")
    result.groupby("timestamp")

    sys.stdout.write("\rgetting formatted string from timestamp...")
    result["timestamp"] = result["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")

    sys.stdout.write("\rconverting to jsonl file...               ")
    result.to_json(args.path_to_merged_log, orient="records", lines=True)


if __name__ == '__main__':
    main()
