class NotificationModel:
    def __init__(self, message, ttl, creation_date, notification_category):
        self.id=0
        self.message=message
        self.ttl=ttl
        self.creation_date
        self.notification_category=notification_category
        self.display_times=0
        self.displayed_once=False

        