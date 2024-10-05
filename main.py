import re

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

head_content = extract_head("example") # for head stuff

if title_search(head_content):
    print(f"Title is {title_search(head_content)}")

#print("did things")
