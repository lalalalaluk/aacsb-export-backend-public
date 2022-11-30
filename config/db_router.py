class DefaultRouter:
    READ_ONLY_APPS = {"hanglong"}
    READ_ONLY_DB = {"ntub_std"}

    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        if model._meta.app_label in self.READ_ONLY_APPS:
            return "ntub_std"
        return "default"

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        if model._meta.app_label in self.READ_ONLY_APPS:
            return None
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Return True if a relation between obj1 and obj2 should be allowed,
        False if the relation should be prevented,
        or None if the router has no opinion.
        This is purely a validation operation,
        used by foreign key and many to many operations to determine if a relation should be allowed between two objects.
        If no router has an opinion (i.e. all routers return None), only relations within the same database are allowed.
        """
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        if db in self.READ_ONLY_DB or app_label in self.READ_ONLY_APPS:
            return False
        return True
