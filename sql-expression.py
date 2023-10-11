from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData 
)

# executing the instrucrions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# making the connection
with db.connect() as connection:
    