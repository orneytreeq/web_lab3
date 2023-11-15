from jinja2 import Template

dict = {
 1: "синий",
 2: "зеленый",
 3: "красный"
}




f_template = open('test_template.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
template = Template(html)
result_html = template.render(dict = dict, int=1)
f = open('test.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()
