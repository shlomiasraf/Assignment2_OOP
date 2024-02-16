class followable:
    def __init__(self):
        self.__followers = []
    def add_follower(self, follower):
        if follower not in self.__followers:
            self.__followers.append(follower)
            return True
        return False
    def remove_follower(self, follower):
        if follower in self.__followers:
            self.__followers.remove(follower)
            return True
        return False
    def notify_followers(self, notification):
        for follower in self.__followers:
            follower.notify(notification)
    def followers_number(self):
        return len(self.__followers)
class follower:

    def __init__(self, username):
        self.__notifications = []
        self.__username = username
    def start_following(self, user):
        return user.add_follower(self)
    def stop_following(self, followable):
        return followable.remove_follower(self)
    def notify(self, notification):
        self.__notifications.append(notification)
    def print_notifications(self):
        print(self.__username + "'s notifications:")
        for notification in self.__notifications:
            print(notification)