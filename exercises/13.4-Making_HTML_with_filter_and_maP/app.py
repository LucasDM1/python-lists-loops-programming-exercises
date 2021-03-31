all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(color):
    if (color["sexy"]== True):
        return (color)

def generate_li(color):
    return ("<li>"+color["label"]+"</li>")

colors=list(filter(filter_colors, all_colors))

htmlcol=list(map(generate_li, colors))
str1=''
str1=str1.join(htmlcol)
print(str1)
