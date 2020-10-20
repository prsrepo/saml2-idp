from sp_certificates import CERTIFICATE as DOCEBO_CERTIFICATE


SAML2_SERVICE_PROVIDERS = [
    {
        'CLASS': 'saml2_idp.sp.docebo_service.AttributeSPHandler',
        'OPTIONS': {
            'display_name': 'Docebo Service Provider',
            'entity_id': 'http://pr.localhost.com:9000/saml/metadata.xml',
            'acs_url': 'http://pr.localhost.com:9000/saml/acs/',
            'certificate': DOCEBO_CERTIFICATE,
        },
    }
]

