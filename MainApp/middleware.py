from django.shortcuts import redirect

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Liste des vues ne nécessitant pas d'authentification
        excluded_paths = ['/', '/explore/', '/loginAndRegister/']

        # Vérifier si l'utilisateur n'est pas authentifié et que la vue nécessite une authentification
        if not request.user.is_authenticated and request.path_info not in excluded_paths:
            # Rediriger vers la page de connexion si la vue nécessite une authentification
            return redirect('/loginAndRegister/')

        return response
