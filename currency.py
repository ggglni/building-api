from flask import Flask, jsonify

#code to scrap data from web
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_= 'ccOutputRslt').get_text()
    rate = float(rate[:-4])
    
    return rate


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency rate API<h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>') #in_cur and #out_cur are the parameters we want to convert into
def api(in_cur, out_cur):
    #scrape currency rate somewhere on web and return it through the API
    rate = get_currency(in_cur, out_cur)
    result_dictionary = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': rate}
    return jsonify(result_dictionary)
    

app.run(host='0.0.0.0')
    