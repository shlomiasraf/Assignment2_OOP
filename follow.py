class followable:
    def __init__(self):
        self.__followers = []
    """
    @brief: updates the followers of this followable that follower started following.
    @param follower: the user that started following this followable.
    @return: True if the follower isn't already following this followable and the update is successful.
    """
    def add_follower(self, follower):
        if follower not in self.__followers:
            self.__followers.append(follower)
            return True
        return False
    """
    @brief: updates the followers of this followable that follower unfollowed.
    @param follower: the user that unfollowed this followable.
    @return: True if the follower is following this followable and the update is successful.
    """
    def remove_follower(self, follower):
        if follower in self.__followers:
            self.__followers.remove(follower)
            return True
        return False
    """
    @brief: notifies the followers of this followable the notification.
    @param notification: the notification we want to notify.
    """
    def notify_followers(self, notification):
        for follower in self.__followers:
            follower.notify(notification)
    """
    @brief: gets the number of followers of this followable.
    """
    def followers_number(self):
        return len(self.__followers)
class follower:

    def __init__(self, username):
        self.__notifications = []
        self.__username = username
    """
    @brief: updates the followers of the user that this follower started following.
    @param user: the user that this follower started following.
    """
    def start_following(self, user):
        return user.add_follower(self)
    """
    @brief: updates the followers of the user that this follower unfollowed.
    @param followable: the user that this follower unfollowed.
    """
    def stop_following(self, followable):
        return followable.remove_follower(self)
    """
    @brief: updates the notifications of this follower.
    @param notification: the notification we want to add to notifications.
    """
    def notify(self, notification):
        self.__notifications.append(notification)
    """
    @brief: print the notifications of this follower.
    """
    def print_notifications(self):
        print(self.__username + "'s notifications:")
        for notification in self.__notifications:
            print(notification)