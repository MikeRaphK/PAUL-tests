from pathlib import Path

import hashlib
import re
import subprocess
import sys

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

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
        print(f"=============== {name} ===============")

        # Make sure the test fails first
        pytest_cmd = ["pytest", test_file]
        result = subprocess.run(pytest_cmd, capture_output=True)
        if result.returncode == 0:
            print(f"ERROR: Test 'pytest {test_file}' did not fail as expected. Exiting...")
            sys.exit(1)

        # Hash test file before running PAUL
        original_test_hash = hash_file(test_file)

        # Run PAUL
        paul_cmd = ["python3", PAUL, "local", "--path", REPO, "--issue", issue_file]
        output = ""
        with subprocess.Popen(paul_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
            for line in proc.stdout:
                print(line, end='')   # Print live
                output += line        # Collect output

        # Re-hash and compare test file
        new_test_hash = hash_file(test_file)
        if new_test_hash != original_test_hash:
            print(f"ERROR: Test file '{test_file}' was modified during repair. Exiting...")
            sys.exit(1)

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

    print(f"All tests completed successfully with ${total_cost:.6f} total cost.")