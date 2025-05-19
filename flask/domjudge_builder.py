import os
from generate_pdf import create_problem_pdf


def build_problem_package(data):
    base_dir = f"output/{data['title'].replace(' ', '_')}"
    sample_dir = os.path.join(base_dir, "data/sample")
    secret_dir = os.path.join(base_dir, "data/secret")
    os.makedirs(sample_dir, exist_ok=True)
    os.makedirs(secret_dir, exist_ok=True)

    # Write sample files
    with open(os.path.join(sample_dir, "1.in"), "w") as f:
        f.write(data['sample_input'])
    with open(os.path.join(sample_dir, "1.ans"), "w") as f:
        f.write(data['sample_output'])

    # Write secret files
    for i, case in enumerate(data['secret'], 1):
        with open(os.path.join(secret_dir, f"{i}.in"), "w") as f:
            f.write(case['input'])
        with open(os.path.join(secret_dir, f"{i}.ans"), "w") as f:
            f.write(case['output'])

    # Create problem.pdf
    create_problem_pdf(data, os.path.join(base_dir, "problem.pdf"))

    # Write domjudge-problem.ini
    ini_content = f"""timelimit = {data.get('time_limit', 2)}
memorylimit = {data.get('memory_limit', 512)}
outputlimit = {data.get('output_limit', 4096)}
"""
    with open(os.path.join(base_dir, "domjudge-problem.ini"), "w") as f:
        f.write(ini_content)

    return base_dir
