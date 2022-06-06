import justpy as jp

class Home():
    path = '/'

    def serve(self):
         wp = jp.QuasarPage(tailwind=True)
         div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
         jp.Div(a=div, text='This is the home page!', classes='text-4xl m-2')
         jp.Div(a=div, text="""Quantum computing is a type of computation that harnesses the collective properties of quantum
                               states, such as superposition, interference, and entanglement, to perform calculations. 
                               The devices that perform quantum computations are known as quantum computers.
                               [1]: I-5  Though current quantum computers are too small to outperform usual 
                               (classical) computers for practical applications, they are believed to be capable of solving 
                               certain computational problems, such as integer factorization (which underlies RSA encryption),
                               substantially faster than classical computers.[2] The study of quantum computing is a subfield 
                               of quantum information science.""", classes='text-lg')
         return wp
