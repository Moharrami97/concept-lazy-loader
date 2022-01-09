# I want to make a stable connection for all 3 classes,
# but do not use MongoHandler at first,
# and  call MongoHandler in certain situations.

from time import sleep


class LazyLoader:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class MySqlHandler:
    def __init__(self):
        sleep(1)

    def get(self):
        return "Hello from MySql"


class MongoHandler:
    def __init__(self):
        sleep(100)

    def get(self):
        return "Hello from Mongo"


class NotificationCenterHandler:
    def __init__(self):
        sleep(1)

    def get(self):
        return "Hello from Notification"


if __name__ == "__main__":
    mysql = LazyLoader(MySqlHandler)
    mongo = LazyLoader(MongoHandler)
    notification = LazyLoader(NotificationCenterHandler)

    print(mysql.get())
    print(notification.get())
