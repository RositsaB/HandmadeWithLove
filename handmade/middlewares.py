from handmade.common.views import InternalErrorView, Error404View


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return Error404View(response)
        elif response.status_code >= 500:
            return InternalErrorView.as_view()(response)

        return response

    return middleware
