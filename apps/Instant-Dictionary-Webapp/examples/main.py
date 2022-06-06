import justpy as jp

@jp.SetRoute('/home')
def home():
    # create a webpage instance
    wp = jp.WebPage()
    jp.Div(a=wp, text='Hello world/home', 
           classes='text-orange-900 bg-yellow-500 font-serif text-lg')
    jp.Div(a=wp, text='Hello agin/home!!')
    return wp

@jp.SetRoute('/about')
def about():
    wp = jp.WebPage()
    jp.Div(a=wp, text='Hello world/about')
    jp.Div(a=wp, text='Hello agin/about!!')
    return wp

# connect the webpage instance to a URL
#jp.Route('/', home) # (path , request handler)

# start the server
jp.justpy()