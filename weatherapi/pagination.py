from rest_framework.pagination import PageNumberPagination

class PageNumberPaginationn(PageNumberPagination):
    page_size = 10
    last_page_strings = ('end',)
