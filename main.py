# I want to make a stable connection for all 3 classes,
# but do not use MongoHandler at first,
# and  call MongoHandler in certain situations.


class MySqlHandler:
    pass


class MongoHandler:
    pass


class NotificationCenterHandler:
    pass


if __name__ == "__main__":
    mysql = MySqlHandler()
    mongo = MongoHandler()
    notification = NotificationCenterHandler()
