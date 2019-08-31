from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jsonpify import jsonify
import re, random, string
from data_transfer import get_shortcode, create_url, update_shortcode

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


def custom_error(status_code, message):
    response = jsonify({
        'message': message,
    })
    response.status_code = status_code
    return response


def shorten_success(shortcode):
    response = jsonify({
        'shortcode': shortcode,
    })
    response.status_code = 201
    return response


def stats_success(created, last_redirect, redirect_count):
    response = jsonify({
        'created': created,
        'lastRedirect': last_redirect,
        'redirectCount': redirect_count,
    })
    response.status_code = 200
    return response


def get_success(url):
    response = jsonify({})
    response.status_code = 302
    response.headers['Location'] = url
    return response


def validate(shortcode):
    condition = False
    if len(shortcode) == 6 and re.match(r'^\w+$', shortcode):
        condition = True
    return condition


def generate_shortcode():
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + "_") for _ in range(6))


def shortcode_exists(shortcode):
    response = False
    if get_shortcode(shortcode)['data'] != []:
        response = True
    return response


class UrlShorten(Resource):
    @staticmethod
    def post():
        json_data = request.get_json(force=True)

        if 'url' in json_data:
            url = json_data['url']
        else:
            return custom_error(400, "Url not present")

        if 'shortcode' in json_data:
            shortcode = json_data['shortcode']
            if shortcode_exists(shortcode):
                return custom_error(409, "Shortcode already in use")
        else:
            shortcode = generate_shortcode()

        if validate(shortcode) is False:
            return custom_error(412, "The provided shortcode is invalid")

        create_url(url, shortcode)

        return shorten_success(shortcode)


class Stats(Resource):
    @staticmethod
    def get(shortcode):
        data = get_shortcode(shortcode)
        if data['data'] != []:
            data = get_shortcode(shortcode)
            created_at = data['data'][0]['CreatedAt']
            last_redirect = data['data'][0]['LastRedirect']
            redirect_count = data['data'][0]['RedirectCount']
            return stats_success(created_at, last_redirect, redirect_count)
        else:
            return custom_error(404, "Shortcode not found")


class Shortcode(Resource):
    @staticmethod
    def get(shortcode):
        data = get_shortcode(shortcode)
        if data['data'] != []:
            update_shortcode(shortcode)
            url = data['data'][0]['Url']
            return get_success(url)
        else:
            return custom_error(404, "Shortcode not found")


api.add_resource(UrlShorten, '/shorten')
api.add_resource(Stats, '/<shortcode>/stats')
api.add_resource(Shortcode, '/<shortcode>')

if __name__ == '__main__':
    app.run(debug=True)