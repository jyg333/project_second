from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from test01.models import Samsung, Naver, Kakao, LGEnSol
from django.http import JsonResponse


# def html_temp(article_tag, id=None):
#
#     global topics
#     contextUI = ''
#     if id != None:
#         contextUI = f'''
#             <li>
#                 <form action="/delete/" method ="post">
#                     <input type="hidden" name="id" value={id}>
#                     <input type="submit" value = "delete">
#                 </form>
#             </li>
#             <li><a href ="/update/{id}">update</a></li>
#             '''
#
#     ol = ''
#     for topic in topics:
#         # ol = ''
#         ol += f'<li><a href="/read/{topic["id"]}">{topic["body"]}</a></li>'
#
#     return f"""
#         <html>
#             <body>
#                 <h1><a href = "/">Django</a></h1>
#                     <ol>
#                         {ol}
#                     </ol>
#                 <ul>{article_tag}</ul>
#                 <ul>
#                     <li><a href = "/create/">Create</a><li>
#                     {contextUI}
#                 </ul>
#             </body>
#         </html>
#         """


# @csrf_exempt
# def create(request):
#     global nextId
#
#     if request.method =="GET":
#         article = '''
#             <form action="/create/" method="post">
#                 <p><input type="text" name = "title" placeholder="title"></p>
#                 <p><textarea name = "body" placeholder = "body"></textarea></p>
#                 <p><input type ="submit"></p>
#             </form>
#         '''
#         return HttpResponse(html_temp(article))
#     elif request.method == "POST":
#         title = request.POST["title"]
#         body = request.POST["body"]
#         new_topic = {"id":nextId, "title": title, "body":body}
#         topics.append(new_topic)
#         url = '/read/'+str(nextId)
#
#
#         nextId += 1
#
#
#         return redirect(url)
#
#
# def read(request, id):
#
#     global topics
#
#     article = ''
#
#     for topic in topics:
#         if topic['id'] == int(id):
#             article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
#
#
#     return HttpResponse(html_temp(article,id))
#
# @csrf_exempt
# def delete(request):
#     global topics
#
#     if request.method == "POST":
#         id = request.POST['id']
#
#         newtopics = []
#         for topic in topics:
#             if topic['id'] != int(id):
#                 newtopics.append(topic)
#         topics = newtopics
#
#         return redirect('/')
#
# @csrf_exempt
# def update(request, id):
#
#     global topics
#
#     if request.method == "GET":
#
#         for topic in topics:
#             if topic['id'] == int(id):
#                 selected_topic ={
#                     "title":topic["title"],
#                     "body":topic["body"]
#                 }
#         article = f'''
#                             <form action="/update/{id}/" method="post">
#                                 <p><input type="text" name = "title" placeholder="title" value={selected_topic["title"]}></p>
#                                 <p><textarea name = "body" placeholder = "body" >{selected_topic['body']}</textarea></p>
#                                 <p><input type ="submit"></p>
#                             </form>
#                         '''
#         return HttpResponse(html_temp(article, id))
#
#     elif request.method =="POST":
#
#         title = request.POST['title']
#         body = request.POST['body']
#         for topic in topics:
#             if topic["id"] == int(id):
#                 topic["title"] = title
#                 topic["body"] = body
#
#
#
#         return redirect(f'/read/{id}')


from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View

def get_data(request,  *args, **kwargs):


    return JsonResponse()

class HomeView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'chart_samsung.html')


class NaverHome(View):

    def get(self,request,*args, **kwargs):

        return render(request, 'chart_naver.html')

class LGHome(View):

    def get(self,request,*args, **kwargs):

        return render(request, 'chart_lg.html')

class KakaoHome(View):

    def get(self,request,*args, **kwargs):

        return render(request, 'chart_kakao.html')

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
            # ============================================================
        naver_price_data = []
        naver_date_data = []
        naver_pos_data = []
        naver_nega_data = []
        naver_neu_data = []
        naver_price = Naver.objects.values_list('price')
        naver_date = list(Naver.objects.values_list('date'))
        naver_pos = Naver.objects.values_list('positive')
        naver_nega = Naver.objects.values_list('negative')
        naver_neu = Naver.objects.values_list('neutral')

        n = len(price)
        for i in range(n):
            naver_price_data.append(naver_price[i][0])
            naver_date_data.append(list(naver_date[i]))
            naver_pos_data.append(list(naver_pos[i]))
            naver_nega_data.append(list(naver_nega[i]))
            naver_neu_data.append(list(naver_neu[i]))

            #=================================

        kakao_price_data = []
        kakao_date_data = []
        kakao_pos_data = []
        kakao_nega_data = []
        kakao_neu_data = []
        kakao_price = Kakao.objects.values_list('price')
        kakao_date = list(Kakao.objects.values_list('date'))
        kakao_pos = Kakao.objects.values_list('positive')
        kakao_nega = Kakao.objects.values_list('negative')
        kakao_neu = Kakao.objects.values_list('neutral')

        n = len(price)
        for i in range(n):
            kakao_price_data.append(kakao_price[i][0])
            kakao_date_data.append(list(kakao_date[i]))
            kakao_pos_data.append(list(kakao_pos[i]))
            kakao_nega_data.append(list(kakao_nega[i]))
            kakao_neu_data.append(list(kakao_neu[i]))

            # =======================================
        lg_price_data = []
        lg_date_data = []
        lg_pos_data = []
        lg_nega_data = []
        lg_neu_data = []
        lg_price = LGEnSol.objects.values_list('price')
        lg_date = list(LGEnSol.objects.values_list('date'))
        lg_pos = LGEnSol.objects.values_list('positive')
        lg_nega = LGEnSol.objects.values_list('negative')
        lg_neu = LGEnSol.objects.values_list('neutral')

        n = len(price)
        for i in range(n):
            lg_price_data.append(lg_price[i][0])
            lg_date_data.append(list(lg_date[i]))
            lg_pos_data.append(list(lg_pos[i]))
            lg_nega_data.append(list(lg_nega[i]))
            lg_neu_data.append(list(lg_neu[i]))

            # =======================================

        data = {
            "date": date_data,
            "price": price_data,
            'pos': pos_data,
            'nega': nega_data,
            'neu': neu_data,

            "naver_date": naver_date_data,
            "naver_price": naver_price_data,
            'naver_pos': naver_pos_data,
            'naver_nega': naver_nega_data,
            'naver_neu': naver_neu_data,

            "lg_date": lg_date_data,
            "lg_price": lg_price_data,
            'lg_pos': lg_pos_data,
            'lg_nega': lg_nega_data,
            'lg_neu': lg_neu_data,

            "kakao_date": kakao_date_data,
            "kakao_price": kakao_price_data,
            'kakao_pos': kakao_pos_data,
            'kakao_nega': kakao_nega_data,
            'kakao_neu': kakao_neu_data,


        }
        return Response(data)


