from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_problem_pdf(data, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 40

    def draw_line(text):
        nonlocal y
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(50, y, text)
        y -= 20

    draw_line(f"Title: {data['title']}")
    draw_line("")

    draw_line("Problem Statement:")
    for line in data['statement'].split('\n'):
        draw_line(line)

    draw_line("")
    draw_line("Constraints:")
    for constraint in data['constraints']:
        draw_line(f"- {constraint}")

    draw_line("")
    draw_line("Input Format:")
    draw_line(data['input_format'])

    draw_line("")
    draw_line("Output Format:")
    draw_line(data['output_format'])

    draw_line("")
    draw_line("Sample Input:")
    draw_line(data['sample_input'])

    draw_line("")
    draw_line("Sample Output:")
    draw_line(data['sample_output'])

    c.save()
