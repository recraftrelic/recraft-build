from domain import add_a_sub_domain
from create_app import create_app


def main():
    domain_name = input("What is the name of subdomain?\n")

    if domain_name is None:
        print("Please specify the name")
        main()

    add_a_sub_domain(domain_name)
    add_a_sub_domain("www." + domain_name)

    app_name = input("What is the app name?\n")

    if app_name is None:
        return

    origin = input("Add git origin\n")

    if origin is None:
        return

    create_app(app_name, origin)


if __name__ == '__main__':
    main()
