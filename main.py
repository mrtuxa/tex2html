import re
from bs4 import BeautifulSoup

true = True


def getExampleDir():
    return "./tests"


def getExampleFile(file):
    return open(f'{getExampleDir()}/{file}.tex', 'r')


def extract_content(file):
    with getExampleFile(f'{file}') as f:
        latex_code = f.read()

        pattern = r"\\begin{html}(.*)\\end{html}"

        match = re.search(pattern, latex_code, re.DOTALL)

        if match:
            head_content = match.group(1)
            return head_content.strip()
        else:
            "head cum cum >~<"


def extract_head(file):
    with getExampleFile(f'{file}') as f:
        latex_code = f.read()
        pattern = r"\\begin{head}(.*)\\end{head}"
        match = re.search(pattern, latex_code, re.DOTALL)
        if match:
            head_content = match.group(1)
            return head_content.strip()
        else:
            return None


def extract_body(file):
    with getExampleFile(f'{file}') as f:
        latex_code = f.read()
        pattern = r"\\begin{body}(.*)\\end{body}"
        match = re.search(pattern, latex_code, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            return None


file = getExampleFile('example')

# body_content = extract_body_content("example")
# print(body_content)

content = extract_content("example")

testFile = open("test.html", "a")


def tag_search(tag):
    tagPattern = r"\\" + tag + "{(.*)}"

    tagMatches = re.findall(tagPattern, content)
    for a in tagMatches:
        testFile.write(f"<{tag}>{a}</{tag}>\n")


def title_search(head_content):
    titlePattern = r"\\title{(.*)}"
    matches = re.search(titlePattern, head_content)
    if matches:
        title = matches.group(1).strip()
        return title
    else:
        return None


head_content = extract_head("example")  # for head stuff


def get_head():
    _c = extract_head("example")

    title_pattern = r"\\title{(.*)}"

    return re.findall(title_pattern, _c, re.DOTALL)


def get_body():
    _c = extract_body("example")

    pattern = r"\\.*{(.*)}"

    return re.findall(pattern, _c)


def get_tag():
    _c = extract_body("example")

    pattern = r"\\(\w+)"

    return re.findall(pattern, _c)


template = f"""
   <html>
    <head>
        <title>{get_head()[0]}</title>
    </head>
        <body>
"""

for body, tag in zip(get_body(), get_tag()):
    template += f"<{tag}>{body}</{tag}>\n"

template += """
        </body>
   </html>
   """


def writeHead():
    testFile.write("<head>\n")
    if title_search(head_content):
        testFile.write(f"<title>{title_search(head_content)}</title>\n")
    testFile.write("</head>")


def writeFile():
    with open('test.html', 'w') as testFile:
        testFile.write(BeautifulSoup(template, 'html.parser').prettify())
    print("successfully")


writeFile()
