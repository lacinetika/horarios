from network_endpoints import GANCIO_PLACES
from network_service import NetworkService
from secrets import GANCIO_USER, GANCIO_PASS
from settings import GANCIO_URL


def main():
    # start_bot()
    ns = NetworkService(GANCIO_URL)
    ns.login(GANCIO_USER, GANCIO_PASS)
    places = ns.get(GANCIO_PLACES)
    print(places)

if __name__ == '__main__':
    main()