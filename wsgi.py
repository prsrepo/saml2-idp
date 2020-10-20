from saml2_idp.app import get_wsgi_app


application = get_wsgi_app()


if __name__ == '__main__':
    application.run(host='pr.localhost.com',
                    debug=True,
                    port=8001)
