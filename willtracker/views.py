from django.shortcuts import render

# Create your views here.
# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
import binascii
import ipfsapi
from secretsharing import BitcoinToB58SecretSharer
from flask import Flask, render_template, request, Response
from Crypto.PublicKey import RSA

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
 			template_name = "Asset Records.html"

class RetrieveRecords(TemplateView):
 			template_name = "retrieve records.html"

class ViewRecord(TemplateView):
 			template_name = "view record.html"