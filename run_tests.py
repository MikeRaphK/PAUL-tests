from pathlib import Path

import re
import subprocess
import sys

if __name__ == "__main__":
    # Get path
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <PAUL main.py path> <PAUL-tests path>")
        print(f"Example: python3 {sys.argv[0]} /app/main.py ./local/PAUL-tests/")
        sys.exit(1)
    PAUL = sys.argv[1]
    REPO = sys.argv[2]

    # Get directories
    src_dir = Path(f"{REPO}/src")
    test_dir = Path(f"{REPO}/tests")
    issue_dir = Path(f"{REPO}/issues")

    # For each Python file in the source directory
    total_cost = 0.0
    for src_file in src_dir.glob("*.py"):
        # Skip __init__.py
        if src_file.name == "__init__.py":
            continue

        # Prepare file paths
        name = src_file.stem
        test_file = test_dir / f"test_{name}.py"
        issue_file = issue_dir / f"{name}_issue.txt"
        print(f"Running PAUL on {issue_file}'\n")

        # Make sure the test fails first
        pytest_cmd = ["pytest", test_file]
        result = subprocess.run(pytest_cmd, capture_output=True)
        if result.returncode == 0:
            print(f"ERROR: Test 'pytest {test_file}' did not fail as expected. Exiting...")
            sys.exit(1)

        # Run PAUL
        paul_cmd = ["python3", PAUL, "local", "--path", REPO, "--issue", issue_file]
        result = subprocess.run(paul_cmd, capture_output=True, text=True, timeout=120)
        output = result.stdout

        # Make sure the test passes after
        result = subprocess.run(pytest_cmd, capture_output=True)
        if result.returncode != 0:
            print(f"ERROR: Test 'pytest {test_file}' did not pass as expected. Exiting...")
            sys.exit(1)

        # Find the cost
        match = re.search(r"Total Cost \(USD\):\s*([0-9.]+)", output)
        if not match:
            print(f"Could not find cost for {issue_file}. Exiting...")
            sys.exit(1)
        total_cost += float(match.group(1))

    print(f"All tests completed successfully with {total_cost:.6f} total cost.")