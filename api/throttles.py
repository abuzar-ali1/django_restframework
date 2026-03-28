from rest_framework.throttling import UserRateThrottle


class ZarRateThrottle(UserRateThrottle):
    scope = 'Zar'