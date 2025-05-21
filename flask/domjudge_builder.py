import os
import shutil
import yaml
from generate_pdf import create_problem_pdf

def build_problem_package(data):
    base_dir = f"output/{data['title']}"
    accepted_dir = os.path.join(base_dir, "accepted")
    sample_dir = os.path.join(base_dir, "data/sample")
    secret_dir = os.path.join(base_dir, "data/secret")
    checker_dir = os.path.join(base_dir, "output_validators/checker")
    statement_dir = os.path.join(base_dir, "problem_statement")

    # Create necessary directories
    os.makedirs(accepted_dir, exist_ok=True)
    os.makedirs(sample_dir, exist_ok=True)
    os.makedirs(secret_dir, exist_ok=True)
    os.makedirs(statement_dir, exist_ok=True)

    # Copy validator code from root
    root_checker_path = "output_validators/checker"  # Path to reusable validator
    if os.path.exists(root_checker_path):
        shutil.copytree(root_checker_path, checker_dir, dirs_exist_ok=True)
    else:
        print("⚠️ Warning: Checker directory not found. Skipping validator copy.")

    # Write sample test case
    with open(os.path.join(sample_dir, "01.in"), "w") as f:
        f.write(data['sample_input'])
    with open(os.path.join(sample_dir, "01.ans"), "w") as f:
        f.write(data['sample_output'])

    # Write secret test cases
    for i, case in enumerate(data['secret'], 1):
        with open(os.path.join(secret_dir, f"{i:02d}.in"), "w") as f:
            f.write(case['input'])
        with open(os.path.join(secret_dir, f"{i:02d}.ans"), "w") as f:
            f.write(case['output'])

    # Save accepted solutions if provided
    if 'submit_cpp' in data:
        with open(os.path.join(accepted_dir, "submit.cpp"), "w") as f:
            f.write(data['submit_cpp'])
    if 'submit_py' in data:
        with open(os.path.join(accepted_dir, "submit.py"), "w") as f:
            f.write(data['submit_py'])

    # Generate problem.pdf
    create_problem_pdf(data, os.path.join(statement_dir, "problem.pdf"))

    # Write domjudge-problem.ini
    ini_content = f"""short-name = {data.get('short_name')}
timelimit = {data.get('time_limit', 1.0)}
color = {data.get('color', '#FF0000')}
externalid = {data.get('external_id')}
"""
    with open(os.path.join(base_dir, "domjudge-problem.ini"), "w") as f:
        f.write(ini_content)

    # Write problem.yaml
    yaml_data = {
        "name": data.get("name", "Max of Four"),
        "limits": {
            "memory": data.get("limits", {}).get("memory", 256)
        },
        "validation": data.get("validation", "custom")
    }
    with open(os.path.join(base_dir, "problem.yaml"), "w") as f:
        yaml.dump(yaml_data, f, sort_keys=False)

    return base_dir
