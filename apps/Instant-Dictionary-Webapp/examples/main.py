import justpy as jp

@jp.SetRoute('/home')
def home():
    # create a webpage instance
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

    div1 = jp.Div(a=div, classes='grid grid-cols-3 gap-4 p-4 border border-black')
    jp.Input(a=div1, placeholder='Enter first value', classes='form-input')
    jp.Input(a=div1, placeholder='Enter second value', classes='form-input')
    jp.Div(a=div1, text='Results goes here....', classes='text-gray-600')
    jp.Div(a=div1, text='Just another div....', classes='text-gray-600')
    jp.Div(a=div1, text='Yet another div....', classes='text-gray-600')

    div2 = jp.Div(a=div, classes='grid grid-cols-2 gap-4')
    jp.Button(a=div2, text='Calculate', classes='border border-blue-500 m- py-1 px-4 rounded'
                                              'text-blue-600 hover:bg-red-500 hover:text-white')

    jp.Div(a=div2, text='I am a cool interactive div!!')
    # jp.Div(a=wp, text='Hello world/home', 
    #        classes='text-orange-900 bg-yellow-500 font-serif text-lg')
    # jp.Div(a=wp, text='Hello agin/home!!')
    return wp

# @jp.SetRoute('/about')
# def about():
#     wp = jp.WebPage()
#     jp.Div(a=wp, text='Hello world/about')
#     jp.Div(a=wp, text='Hello agin/about!!')
#     return wp

# connect the webpage instance to a URL
#jp.Route('/', home) # (path , request handler)

# start the server
jp.justpy()