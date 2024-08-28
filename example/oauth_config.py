import os
from oauthlib.oauth2 import WebApplicationClient
from requests_oauthlib import OAuth2Session

client_id = 'your_client_id'
client_secret = 'your_client_secret'

class OAuthConfig:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_flow = OAuth2Session(client_id)

    def get_token(self):
        authorization_url, state = self.oauth_flow.authorization_url('https://example.com/oauth/authorize')
        print(f'Please go to {authorization_url} and authorize access.')
        authorization_response = input('Enter the full callback URL: ')
        try:
            token = self.oauth_flow.fetch_token('https://example.com/oauth/token', client_secret=self.client_secret, authorization_response=authorization_response)
            return token
        except Exception as e:
            print(f'Error occurred while fetching token: {e}')
            return None

    def fetch_protected_resource(self, token):
        if token:
            self.oauth_flow.token = token
            try:
                response = self.oauth_flow.get('https://example.com/protected-resource')
                if response.status_code == 200:
                    print(response.content)
                else:
                    print(f'Error occurred while fetching protected resource: {response.status_code}')
            except Exception as e:
                print(f'Error occurred while fetching protected resource: {e}')

def main():
    oauth_config = OAuthConfig(client_id, client_secret)
    token = oauth_config.get_token()
    if token:
        oauth_config.fetch_protected_resource(token)

if __name__ == '__main__':
    main()