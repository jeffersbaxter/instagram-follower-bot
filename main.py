from insta_follower import InstaFollower

insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

insta_bot.driver.quit()
