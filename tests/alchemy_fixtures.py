from collections import OrderedDict

from sqlalchemy import MetaData, create_engine

from pga.connections import create_alchemy_engine


class AlchemySQLFixture(object):

    @classmethod
    def setUpClass(cls):
        cls.postgres_config = {
            'database': 'pga_testing',
            'host': 'localhost'
        }
        cls.engine = create_alchemy_engine(**cls.postgres_config)
        cls.conn = cls.engine.connect()
        cls.class_meta = MetaData()
        cls._prep_db()
        cls.class_meta.create_all(cls.engine)

    @classmethod
    def _prep_db(cls):
        pass

    @classmethod
    def _cleanup_db(cls):
        cls.class_meta.drop_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        cls._cleanup_db()
        cls.conn.close()
        cls.engine.dispose()


def select_table_record_set(engine, table):
    result_query = table.select()
    alchemy_records = engine.execute(result_query).fetchall()
    return set(tuple(row.values()) for row in alchemy_records)


def column_set_equal(columns, other):
    column_set = column_attribute_set(columns)
    other_set = column_attribute_set(other)

    return column_set == other_set


def column_attribute_set(columns) -> set:
    attributes = (get_column_attributes(column) for column in columns)
    attribute_set = set(attributes)

    return attribute_set


def get_column_attributes(column) -> tuple:
    attributes = ['default', 'name', 'nullable', 'type']

    attribute_dict = OrderedDict(
        (attribute, getattr(column, attribute)) for attribute in attributes
    )
    attribute_dict['type'] = str(attribute_dict['type'])
    column_attributes = tuple(attribute_dict)

    return column_attributes


def _dump(sql, *multiparams, **params):
    pass


def create_mock_engine():
    return create_engine('postgresql://', strategy='mock', executor=_dump)
