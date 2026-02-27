import argparse

from svg.pipeline import generate_visualization


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    generate_visualization(args.input, args.output)
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
