from .home import (
    IndexView,
    DetailView,
    vote,
    ResultsView,
)

from .error import (
    pag_400_bad_request,
    pag_403_forbidden,
    pag_404_not_found,
    pag_500_error_server
)


__all__ = [
    'IndexView',
    'DetailView',
    'vote',
    'ResultsView',
    #For HTTP STATUS ERROR CODE
    'pag_400_bad_request',
    'pag_403_forbidden',
    'pag_404_not_found',
    'pag_500_error_server'
]