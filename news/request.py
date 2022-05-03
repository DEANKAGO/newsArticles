from flask import Flask
import urllib3
import json

api_key = None 
base_url = None

def configure_request(app):
  global api_key, base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']

def get_news():
  """
  function to get json to respond to our url request"""
  get_news_url = base_url.format(api_key)