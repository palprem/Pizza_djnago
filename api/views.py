from django.shortcuts import render
from .models import Piza, Size, Toping
from .serializers import PizaSeriaizer, SizeSeriaizer, TopingSeriaizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

class AllAPI(APIView):
    def get(self, request, pk=None,format=None):
        piza=Piza.objects.all()
        size=Size.objects.all()
        dct={}
        dct1={}
        serializer1 =PizaSeriaizer(piza, many=True)
        serializer2 =SizeSeriaizer(size, many=True)
        for i in serializer1.data:
            for j in serializer2.data:
                if i['name'] == j['pname']:
                    dct[i['types']]=j['size']
    
        return Response(dct)

class PizaAPI(APIView):
    def get(self, request, pk=None,format=None):
        stu=Piza.objects.all()
        serializer =PizaSeriaizer(stu, many=True)
        filter_backends= [SearchFilter]
        search_fields=serializer.data['name']
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request,format=None):
        data=request.data
        k=data['name']
        l=data['types']
        if l=='Regular' or l=='Square':
            try:
                emp_data=Piza.objects.get(name=k, types=l)
                return Response({'msg':'present'})
            except:
                serializer=PizaSeriaizer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'data saved'})
        return Response({'msg':'chal be'})

    def delete(self, request, pk, format=None):
        try:
            stu = Piza.objects.get(id=id)
            stu.delete()
            return Response({'mag':'data deleted'}) 
        except:
            return Response({'mag':'wrong id'})

    def put(self, request, pk, format=True):
        id= request.data.get('id')
        data=request.data
        stu=Piza.objects.get(id=id)
        serializer=PizaSeriaizer(stu, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mag':'data update'})


class TopingAPI(APIView):
    def get(self, request, formate=True):
        data=Toping.objects.all()
        serializer=TopingSeriaizer(data, many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        data=request.data
        try:
            emp_data=Toping.objects.get(toping=data)
            return Response({'msg':'present'})
        except:
            serializer=TopingSeriaizer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data saved'})
        return Response({'msg':'chal be'})

class SizeAPI(APIView):
    def get(self, request, formate=None):
        pizaName=Size.objects.all()
        serializer=SizeSeriaizer(pizaName, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        data=request.data
        pname=data['pname']
        size=data['size']
        topi=Piza.objects.all()
        ListOfPizza=''
        for i in topi:
            if pname == i.name:
                ListOfPizza=ListOfPizza+i.name
        # print("List",ListOfPizza)
        if pname in ListOfPizza:
            try:
                Size.objects.get(pname=pname, size=size)
                return Response({'msg':'data already present'})
            except:
                serializer=SizeSeriaizer(data=data)
                if serializer.is_valid():
                    serializer.save()
                return Response({'msg':'data save'})
        return Response({'msg':'add pizza before'})


        