from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.db_model import Base

db_engine = create_engine('postgresql://postgres:password@localhost/database_2')
# Build all the table from our models.
Base.metadata.create_all(db_engine)

Session = sessionmaker(bind=db_engine)
session = Session()
session.commit()
session.close()
