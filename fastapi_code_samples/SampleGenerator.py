import json

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute

from fastapi_code_samples.CustomAuth import CustomAuth


class SampleGenerator:
    def __init__(self,
                 app: FastAPI,
                 API_PREFIX: str = 'http://localhost:8000',
                 BASE_URL: str = '/',
                 auth_config: CustomAuth = CustomAuth(
                     header='X-API-Key',
                     sample_token='1234'
                 )):
        self.app = app
        self.API_PREFIX = API_PREFIX
        self.BASE_URL = BASE_URL
        self.auth_config = auth_config

    def custom_openapi(self):

        openapi_schema = get_openapi(
            title=self.app.title,
            version=self.app.version,
            routes=self.app.routes
        )
        for route in self.app.routes:
            if route.path.startswith('/docs') or route.path.startswith('/redoc'):
                continue
            if route.path.startswith(self.API_PREFIX) and '.json' not in route.path:
                for method in route.methods:
                    try:
                        code_samples = self.get_code_samples(route=route, method=method)
                        openapi_schema["paths"][route.path][method.lower()]["x-codeSamples"] = code_samples
                    except:
                        pass

        self.app.openapi_schema = openapi_schema

        return self.app.openapi_schema

    def get_code_samples(self, route: APIRoute, method):
        nl = '\n'
        if method in ['GET', 'DELETE']:
            auth_header = f"'{self.auth_config.header}': '{self.auth_config.prefix}{self.auth_config.sample_token}'"
            return [
                {
                    'lang': 'Shell',
                    'source': f"curl --location\\{nl} "
                              f"--request {method} '{self.BASE_URL}{route.path}'\\{nl} "
                              f"--header {auth_header}",
                    'label': 'curl'
                },
                {
                    'lang': 'Python',
                    'source': f"import requests{nl}"
                              f"url = \"{self.BASE_URL}{route.path}\"{nl}"
                              f"headers = {{{auth_header}}}{nl}"
                              f"response = requests.request(\"{method}\", url, headers=headers){nl}"
                              f"print(response.text)",
                    'label': 'Python3'
                },
                {
                    'lang': 'JavaScript',
                    'source': f"const axios = require('axios'){nl}"
                              f"const url = \"{self.BASE_URL}{route.path}\"{nl}"
                              f"const headers = {{{auth_header}}}{nl}"
                              f"axios.{method.lower()}(url, {{ headers }}){nl}"
                              f"    .then(response => console.log(response.data)){nl}"
                              f"    .catch(error => console.error(error))",
                    'label': 'Node.js'
                }
            ]
        if method in ['POST', 'PUT', 'PATCH'] and route.body_field:
            try:
                example_schema = route.body_field.type_.Config.json_schema_extra.get('example')
                payload = f"json.dumps({example_schema})"
                data_raw = f"\\{nl} --data-raw " + "'" + f"{json.dumps(example_schema)} " + "'"
            except Exception as e:
                payload = '{}'
                data_raw = ''
        else:
            payload = '{}'
            data_raw = ''
        return [
            {
                'lang': 'Shell',
                'source': f"curl --location\\{nl} "
                          f"--request {method} '{self.BASE_URL}{route.path}'\\{nl} "
                          f"--header 'X-API-Key': '2324143'"
                          f"{data_raw}",
                'label': 'curl'
            },
            {
                'lang': 'Python',
                'source': f"import requests{nl}"
                          f"{'import json' + nl if method.lower() == 'post' else ''}{nl}"
                          f"url = \"{self.BASE_URL}{route.path}\"{nl}"
                          f"payload = {payload}{nl}"
                          f"headers = {{'X-API-Key': '2324143'}}{nl}"
                          f"response = requests.request(\"{method}\", url, headers=headers, data=payload){nl}"
                          f"print(response.text)",
                'label': 'Python3'
            },
            {
                'lang': 'JavaScript',
                'source': f"const axios = require('axios'){nl}"
                          f"const url = \"{self.BASE_URL}{route.path}\"{nl}"
                          f"const headers = {{'X-API-Key': '2324143'}}{nl}"
                          f"const payload = {payload}{nl}"
                          f"axios.{method.lower()}(url, payload, {{ headers }}){nl}"
                          f"    .then(response => console.log(response.data)){nl}"
                          f"    .catch(error => console.error(error))",
                'label': 'Node.js'
            }
        ]
