from django.shortcuts import render

from django.http import HttpResponse
from keycloak import KeycloakOpenID

def index(request):
    keycloak_openid = KeycloakOpenID(server_url="https://keycloak:8443/",
                        client_id="backend",
                        realm_name="demo",
                        client_secret_key="mPhUHv7s9Mo1KoPBCYkj8ZWSiLSJyFH0")
    config_well_know = keycloak_openid.well_know()
    print(config_well_know)
    token = keycloak_openid.token("local", "local")
    print(token)
    return HttpResponse("Hello, world. You're at the polls index.")

