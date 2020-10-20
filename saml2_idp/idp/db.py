import attr


@attr.s
class User:
    username = attr.ib()
    email = attr.ib()
    first_name = attr.ib()
    last_name = attr.ib()


users = {user.username: user for user in [
    User('alex', 'alex@example.com', 'alex', 'samuel'),
    User('jordan', 'jordan@example.com', 'jordan', 'gilbert'),
]}
