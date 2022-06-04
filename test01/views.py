from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from test01.models import Samsung
from django.http import JsonResponse



nextId = 4

topics =[
    {"id":1, "title":"routing", "body":"Routing is"},
    {"id":2, "title":"views", "body":"views is"},
    {"id":3, "title":"models", "body":"models is"},
]
def html_temp(article_tag, id=None):

    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method ="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value = "delete">
                </form>
            </li>
            <li><a href ="/update/{id}">update</a></li>
            '''

    ol = ''
    for topic in topics:
        # ol = ''
        ol += f'<li><a href="/read/{topic["id"]}">{topic["body"]}</a></li>'

    return f"""
        <html> 
            <body>
                <h1><a href = "/">Django</a></h1>
                    <ol>
                        {ol}
                    </ol>
                <ul>{article_tag}</ul> 
                <ul>
                    <li><a href = "/create/">Create</a><li>
                    {contextUI}
                </ul>
            </body>
        </html>    
        """


@csrf_exempt
def create(request):
    global nextId

    if request.method =="GET":
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name = "title" placeholder="title"></p>
                <p><textarea name = "body" placeholder = "body"></textarea></p>
                <p><input type ="submit"></p>
            </form>
        '''
        return HttpResponse(html_temp(article))
    elif request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        new_topic = {"id":nextId, "title": title, "body":body}
        topics.append(new_topic)
        url = '/read/'+str(nextId)


        nextId += 1


        return redirect(url)


def read(request, id):

    global topics

    article = ''

    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'


    return HttpResponse(html_temp(article,id))

@csrf_exempt
def delete(request):
    global topics

    if request.method == "POST":
        id = request.POST['id']

        newtopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newtopics.append(topic)
        topics = newtopics

        return redirect('/')

@csrf_exempt
def update(request, id):

    global topics

    if request.method == "GET":

        for topic in topics:
            if topic['id'] == int(id):
                selected_topic ={
                    "title":topic["title"],
                    "body":topic["body"]
                }
        article = f'''
                            <form action="/update/{id}/" method="post">
                                <p><input type="text" name = "title" placeholder="title" value={selected_topic["title"]}></p>
                                <p><textarea name = "body" placeholder = "body" >{selected_topic['body']}</textarea></p>
                                <p><input type ="submit"></p>
                            </form>
                        '''
        return HttpResponse(html_temp(article, id))

    elif request.method =="POST":

        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic["id"] == int(id):
                topic["title"] = title
                topic["body"] = body



        return redirect(f'/read/{id}')


# def send_data(request):
#
#     labels = list(Samsung.objects.values('price'))
#     data = list(Samsung.objects.values('date'))
#     test_data = Samsung.objects.all()
#     print(test_data)
#
#     return JsonResponse({
#         'price': labels,
#         'date' : data
#     })


from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View

def get_data(request,  *args, **kwargs):

    data = {
        "sales":100,
        "customer":10

    }
    return JsonResponse(data)

class HomeView(View):

    def get(self, request, *args, **kwargs):
        pos = Samsung.objects.values_list('positive')
        nega = Samsung.objects.values_list('negative')
        neu = Samsung.objects.values_list('neutral')

        return render(request, 'charts.html',{"customers": 10})

class ChartData(APIView):

    def get(self, request, format=None):

        price_data = []
        date_data = []
        pos_data = []
        nega_data = []
        neu_data = []
        price = Samsung.objects.values_list('price')
        date = list(Samsung.objects.values_list('date'))
        pos = Samsung.objects.values_list('positive')
        nega = Samsung.objects.values_list('negative')
        neu = Samsung.objects.values_list('neutral')

        n = len(price)
        for i in range(n):
            price_data.append(price[i][0])
            date_data.append(list(date[i]))
            pos_data.append(list(pos[i]))
            nega_data.append(list(nega[i]))
            neu_data.append(list(neu[i]))

        data = {
            "date": date_data,
            "price": price_data,
            'pos': pos_data,
            'nega': nega_data,
            'neu': neu_data
        }
        return Response(data)


