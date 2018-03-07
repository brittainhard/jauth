if __name__ == "__main__":
    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from jauth.dbauth.tables import User

    engine = create_engine('sqlite:///users.sqlite', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    if len(sys.argv) < 3:
        print("Please specify a username and password")
    else:
        session.add(User(username=sys.argv[1], password=sys.argv[2]))
        session.commit()
