from sanic import Sanic
from sanic import request, response

app = Sanic("My Hello, world app")

@app.route('/')
async def test(req):
    return response.json({'hello': 'world'})

@app.route('/test')
def html_test(req):
    return response.file('templates/index.html')

@app.route('/post_route', methods = ['POST'])
def post_func(req):
    print(request)

if __name__ == '__main__':
    app.run(host ="127.0.0.1", port = 3000, debug = True)