# this program will accept argument and return forward geocoded details

import requests
from flask import Flask
from flask import request

def create_app():
    app = Flask(__name__)
    @app.route('/geo', methods=['GET', 'POST'])
    def index():
        q = request.args.get('q')
        url = "https://us1.locationiq.com/v1/search"
        data = {
            'key': 'locationiq-api-key',
            'q': q,
            'format': 'json'
        }

        response = requests.get(url, params=data)
       
        return response.text #you can jsonify and get the boundingbox element for the coverage area
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
