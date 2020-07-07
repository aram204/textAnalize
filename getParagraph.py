from bs4 import BeautifulSoup
html = """
<div>
<p>
1. my text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages, and more recently...
</p>
<p>
2. my text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages, and more recently...
</p>
</div>
"""
soup = BeautifulSoup(html,"lxml")
for tag in soup.find_all("p"):
    print(tag.text)
