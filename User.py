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
    """
    @brief: Prints the username + the number of posts he has + the number of followers he has.
    """
    def __repr__(self):
        return ("User name: " + self.__username +", Number of posts: " + str(self.__postsNumber) + ", Number of followers: "
        + str(self.followers_number()))

    """
    @brief: set the online status of the user.
    @param status: the new online status of the user.
    """
    def set_online_status(self,status):
        self.__isOnline = status

    """
    @brief: get the user name of the user.
    """
    def get_username(self):
        return self.__username
    """
    @brief: get the password of the user.
    """
    def get_password(self):
        return self.__password

    """
    @brief: get the online status of the user.
    """
    def get_isOnline(self):
        return self.__isOnline

    """
    @brief: updates the followers of the user that this user started following.
    @param user: the user that this user started following.
    """
    def follow(self,user):
        if self.__isOnline and self.start_following(user):
            print(self.__username  + " started following " + user.__username)

    """
    @brief: updates the followers of the user that this user unfollowed.
    @param user: the user that this user unfollowed.
    """
    def unfollow(self,user):
        if self.__isOnline and self.stop_following(user):
            print(self.__username + " unfollowed " + user.__username)

    """
    @brief: publish this post.
    @param PostKind: the kind of this post. 
    @param description: the description of this post.
    @param *args: additional variables of the post like price and location.
    @return: this post.
    """
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