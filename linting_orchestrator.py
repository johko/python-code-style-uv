"""
This script redirects the linting for flake8 and pylint to lintly
if we lint a PR and otherwise fails if the specified linter fails.
"""

import argparse
import os
import sys
import subprocess

LINTER_TO_CMD = {
    "flake8": ["flake8", "--extend-exclude=dist,build"],
    "pylint": ["pylint", "--output-format=json"],
}
LINTER_TO_FORMAT = {"flake8": "flake8", "pylint": "pylint-json"}

LINTLY_CMD = [
    "lintly",
    "--api-key",
    os.environ["GITHUB_TOKEN"],
    "--fail-on",
    "any",
    "--post-status",
    "--request-changes",
    "--use-checks",
    "--no-exit-zero",
]


def linter_cmd_defaults(python_files: list[str]):
    if os.path.exists(".pylintrc"):
        LINTER_TO_CMD["pylint"].append("--rcfile=.pylintrc")
    else:
        path = os.path.join(os.environ["GITHUB_ACTION_PATH"], ".pylintrc")
        LINTER_TO_CMD["pylint"].append(f"--rcfile={path}")

    if not python_files:
        print("No lintable python files. Exiting.")
        sys.exit(0)
    else:
        LINTER_TO_CMD[args.linter].extend(python_files)


def main(args: argparse.Namespace) -> None:
    linter_cmd_defaults(args.python_files)

    linting_process = subprocess.run(
        LINTER_TO_CMD[args.linter], capture_output=True, check=False
    )

    if args.is_pull_request == "true":
        LINTLY_CMD.append("--format=" + LINTER_TO_FORMAT[args.linter])
        lintly_process = subprocess.run(
            LINTLY_CMD, input=linting_process.stdout, check=False
        )
        sys.exit(lintly_process.returncode)
    else:
        if linting_process.returncode == 0:
            print("Success: No issues found.")
        else:
            print(linting_process.stdout.decode("utf-8"))
        sys.exit(linting_process.returncode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("is_pull_request", choices=["true", "false"])
    parser.add_argument("linter", choices=LINTER_TO_CMD.keys())
    parser.add_argument("python_files", nargs="+", metavar="python_file")
    args = parser.parse_args()
    main(args)
