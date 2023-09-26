class Twitter:

    def __init__(self):
        self.user = [0 for _ in range(501)]
        self.user_tweet = dict()
        self.user_follow = dict()
        self.num = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.user[userId] == 1:
            heappush(self.user_tweet[userId], (self.num, tweetId))
        else:
            self.user_tweet[userId] = [(self.num, tweetId)]
            self.user_follow[userId] = [userId]
            self.user[userId] = 1
        self.num -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #user_follow를 확인하고 heap만들어서 리턴
        feed = []
        if self.user[userId] == 1:
            feedUsers = self.user_follow[userId]
            for fu in feedUsers:
                if self.user[fu] == 1:
                    for num_tweet in self.user_tweet[fu]:
                        heappush(feed, num_tweet)
            feed_ = []
            for i in range(10):
                if feed == []: break
                feed_.append(heappop(feed)[1])
            return feed_
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.user[followerId] == 0:
            self.user_follow[followerId] = [followerId]
            self.user_tweet[followerId] = []
            self.user[followerId] = 1
        if followeeId not in self.user_follow[followerId]:
            heappush(self.user_follow[followerId], followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follow[followerId]:
            self.user_follow[followerId].remove(followeeId)
            

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)