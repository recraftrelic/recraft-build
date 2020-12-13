from domain import add_a_sub_domain


def main():
    domain_name = input("What is the name of subdomain?")

    if domain_name is None:
        print("Please specify the name")
        main()

    add_a_sub_domain(domain_name)
    add_a_sub_domain("www." + domain_name)

if __name__ == '__main__':
    main()
