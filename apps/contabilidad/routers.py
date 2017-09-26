# disabled config to settings.py
class ContaRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read contabilidad models go to conta.
        """
        if model._meta.app_label == 'contabilidad':
            return 'conta'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write contabilidad models go to conta.
        """
        if model._meta.app_label == 'contabilidad':
            return 'conta'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the contabilidad app is involved.
        """
        if obj1._meta.app_label == 'contabilidad' or \
           obj2._meta.app_label == 'contabilidad':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the contabilidad app only appears in the 'conta'
        database.
        """
        if app_label == 'contabilidad':
            return db == 'conta'
        return None