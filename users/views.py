# users/views.py
from rest_framework import generics

from . import models
from . import serializers
from .models import Asset
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from rest_framework.decorators import api_view


from docx import Document
from docx.shared import Inches

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

@api_view(['GET'])
def get_all_user_asset(request):
    try:
    	assests = Asset.objects.get(user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AssetSerializer(assests)
    return Response(serializer.data)

@api_view(['POST'])
def add_asset(request):
    asset_type = request.POST.get('asset_type', None)
    description = request.POST.get('description', None)
    recipient = request.POST.get('recipient', None)
    relation = request.POST.get('relation', None)
    if not asset_type or not description or not recipient or not relation:
    	error_message = "Missing parameters in request. Send asset_type, description, recipient, relation"
    	return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
    Asset.objects.create(asset_type=asset_type, description=description, recipient=recipient, relation=relation,user=user)
    success_message = "Sucessfully added new assest."
    return Response(success_message, status=status.HTTP_201_CREATED)

def download(request):
    document = Document()

    document.add_heading('Document Title', 0)

    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True

    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='IntenseQuote')

    document.add_paragraph(
    'first item in unordered list', style='ListBullet'
    )
    document.add_paragraph(
    'first item in ordered list', style='ListNumber'
    )

    #document.add_picture('monty-truth.png', width=Inches(1.25))

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'

    document.add_page_break()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    document.save(response)

    return response