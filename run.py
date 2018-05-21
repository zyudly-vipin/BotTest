
import requests
import urllib
import flask 
from flask import Flask, redirect 



@app.route("/", methods=['GET', 'POST'])
def health_check():
    return "Hello!"

if __name__ == "__main__":
    app.run()
