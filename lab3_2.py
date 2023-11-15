from jinja2 import Template

books = [
    {"title" : "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title" : "Белая гвардия",
    "author": "Булгаков М.А.",
      "price": 600.00},
    {"title" : "Война и мир",
    "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title" : "Анна Каренина",
    "author": "Толстой Л.Н.", 
     "price": 450.10},
    {"title" : "Игрок",
    "author": "Достоевский Ф.М.",
    "price":  234.55}
];




f_template = open('test_template2.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
template = Template(html)
result_html = template.render(list = books, first=3, last=2)
f = open('test.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()
