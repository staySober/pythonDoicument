from wxpy import *

# 登录web微信 使用缓存选项
bot = Bot(cache_path=True)
print("wechat login ......")
# 打印接收到的信息
#@bot.register()
#def print_others(msg):
#    print(msg)
# 好友聊天
#my_friend = ensure_one(bot.search('杨帆'))
auto_reply_friend_name = input("please set auto reply's friend")
print ("你输入的好友名称(备注)是: ", auto_reply_friend_name)

auto_reply_group_name = input("please set auto reply's group")
print ("你输入的群聊名称(备注)是: ", auto_reply_group_name)

#tuling
tuling = Tuling(api_key = '862496e8b91f4daf83c251256686e0d7')
print('access to tuling server successfully')
#小i
xiaoi = XiaoI('gTRmcpdlTFjK','v14kKfHGijELHrvc2O9F')
print('access to xiaoi server successfully')

# 群聊
wxpy_groups = bot.groups().search(auto_reply_group_name)
@bot.register(wxpy_groups)
def reply_my_groups(msg):
    try:
        tuling.do_reply(msg)
    except :
        xiaoi.do_reply(msg)
    finally :
        print("auto reply successfully")

# friend
my_friend = ensure_one(bot.search(auto_reply_friend_name))
@bot.register(my_friend)
def reply_my_friend(msg):
    try:
        tuling.do_reply(msg)
    except :
        xiaoi.do_reply(msg)
    finally :
        print("auto reply successfully")

# 后台运行
embed()
