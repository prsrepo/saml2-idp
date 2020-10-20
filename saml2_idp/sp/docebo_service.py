from flask_saml2.idp import SPHandler


class AttributeSPHandler(SPHandler):
    def build_assertion(self, request, *args, **kwargs):
        return {
            **super().build_assertion(request, *args, **kwargs),
            'ATTRIBUTES': {
                'foo': 'bar',
            },
        }
