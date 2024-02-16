from Post import TextPost, ImagePost, SalePost
from follow import followable, follower

class User(followable,follower):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__isOnline = False
        self.__postsNumber = 0
        followable.__init__(self)
        follower.__init__(self, username)

    def __repr__(self):
        return ("User name: " + self.__username +", Number of posts: " + str(self.__postsNumber) + ", Number of followers: "
        + str(self.followers_number()))
    def set_online_status(self,status):
        self.__isOnline = status
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_isOnline(self):
        return self.__isOnline
    def follow(self,user):
        if self.__isOnline and self.start_following(user):
            print(self.__username  + " started following " + user.__username)
    def unfollow(self,user):
        if self.__isOnline and self.stop_following(user):
            print(self.__username + " unfollowed " + user.__username)
    def publish_post(self, PostKind, description, *args):
        if self.__isOnline:
            self.__postsNumber += 1
            self.notify_followers(self.__username + " has a new post")
            post = None
            if PostKind == "Text":
                post = TextPost(description,self)
            elif PostKind == "Image":
                post = ImagePost(description,self)
            elif PostKind == "Sale":
                post = SalePost(description,self , *args)
            print(post)
            return post