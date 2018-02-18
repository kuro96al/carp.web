from settings import set_environments
from app import create_app


def main():
    set_environments()

    application = create_app()
    application.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
