import django_filters
from django.http import HttpResponse
from geopy.distance import vincenty
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import filters
from rest_framework import generics
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.svm import SVR
import numpy as np
import pickle as pickle
clfp = pickle.load(open('modelb.pkl','rb'))
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('BusNo', 'BusRoute')


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('BusNo', 'BusRoute')

#def GetResults(request):#def get_train():
#    if request.method == 'GET':
#       busStopNo = request.GET['val']
#       distance = request.GET['distance']
#       time = request.GET['time']
       #neural network code..
      

def load_model():#make it load once when the service starts. called only once.
	#load_the model
         f = open('bpinall.txt','r').readlines()
         num_rows=len(f)
         num_col=len(f[0].split(','))
         x = np.zeros((num_rows,num_col),dtype=float)
         y=np.zeros((num_rows),dtype=float)
         for i,line in enumerate(f):
           line=line.strip('\r\n').strip()
           if line.count(',')>0:
            x[i]=[float(p) for p in line.split(',')]
         f2=open('bpoutall.txt','r').readlines()
         for i,line in enumerate(f2):
             line=line.strip('\r\n')
             y[i]=float(line)
         clf=ExtraTreesRegressor(verbose=0)
         print (x)
         clf.fit(x[:-1],y[:-1])
         pq=clf.predict(x[-1])
         print (pq,y[-1])
         #global clfp
         pickle.dump(clf,open('modelb.pkl','wb'))
         return pq
         
def GetResults(request):

     if request.method == 'GET':
       busStopNo = request.GET['val']
       distance = request.GET['distance']
       time = request.GET['time']
       
       pq=clfp.predict([busStopNo,distance,time,0.1])
       return HttpResponse("values are " + str (busStopNo) + "" + str(distance) + " " + str(time)+""+str(pq))
